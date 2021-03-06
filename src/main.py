#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################################################
#
#    Il Procione Bot
#    A Telegram bot built for fun
#    Copyright (C) 2018  I Procioni
#    https://github.com/procioni/procioni-bot
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###################################################################################


import environ_check  
#esegui il check di tutte le variabili e di mongodb appena viene importato
#se ci sono errori termina l'esecuzione del bot in automatico
environ_check.check()


#comincia esecuzione del bot

import os, logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, InlineQueryHandler
from telegram.ext.dispatcher import run_async
import dbManager
import language as lan


#recupera le variabili necessarie ad avviare il bot
TOKEN = os.environ.get('TOKEN', 'token')
PORT = int(os.environ.get('PORT', '8443'))
APP_URL = os.environ.get('APP_LINK', '')


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)



# Funzioni #
################################################################################################################################


# comando start
@run_async
def start(bot, update):  
    #controlla se esiste un account con lo stesso TelegramID
    if dbManager.exist_user(update.message.from_user.id) == False:
        #crea account
        dbManager.create_user(update.message.from_user.first_name, update.message.from_user.id)
        lan.send_localized_reply(update, "account_created")
    else:
        #mostra errore
        lan.send_localized_reply(update, "already_own_account")
    
    #controlla se esiste un procione creato per l'account corrente
    if dbManager.exist_raccoon(update.message.from_user.id) == False:
        lan.send_localized_reply(update, "set_raccoon_name")

# imposta nome procione
def setRaccoonName(bot, update):
    if dbManager.exist_raccoon(update.message.from_user.id) == False:
        name = update.message.text
        dbManager.create_raccoon(name, update.message.from_user.id)
        lan.send_localized_reply(update, "new_raccoon",n=name)
    else:
        lan.send_localized_reply(update, "already_own_raccoon")


################################################################################################################################

# funzione principale del bot
def main():
    DEBUG = os.environ.get('DEBUG', "false")

    #crea l'update e il dispatcher
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher


    #aggiungi gli handler di comandi e funzioni
    dispatcher.add_handler(CommandHandler("start", start))

    dispatcher.add_handler(MessageHandler(Filters.text, setRaccoonName))


    #lista dei tipi di update supportati dal bot
    up_kind = ["message"]

    #avvia il bot con webhook se in modalita produzione altrimenti usa il polling per testare in locale
    if DEBUG != "false":
        updater.start_polling(allowed_updates= up_kind)
        print("DEBUG MODE ON")
    else:
        updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN, allowed_updates=up_kind)
        updater.bot.set_webhook(APP_URL + TOKEN)
        print("PRODUCTION MODE")


    updater.idle()


if __name__ == '__main__':
    main()