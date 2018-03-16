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

import json
import os 

my_path = os.path.abspath(os.path.dirname(__file__))
j_path =  os.path.join(my_path, "../data/language.json")

#carica il json dei testi
if not os.path.exists(j_path) or os.path.getsize(j_path) <= 0:
    print ("[CRITICAL ERROR]: Unable to load language file! Please check that data/language.json is present")
    exit(1)

language_fp = open(j_path)

language = json.load(language_fp)

language_fp.close()


# ottieni il testo associato al nome assegnato del json
# id: nome del testo scritto nel json
# user: user di del framework telegram da cui prendere il codice regionale. Se none usa il testo impostato come defalt per l'id richiesto
# se l'id non esiste restituisce un messaggio di errore
def get_text(id, user=None):

    code = ""

    if user is None:
        code = "default"
    else:
        code = user.language_code

    if not id in language:
        return "Missing language key: "+id
    
    if code in language[id]:
        return language[id][code]
    else:
        return language[id]["default"]

#invia una risposta localizzata in base al codice regionale dell'utente
#supporta solo gli update contenenti message
#e' possibile passare una serie di parametri con nome che vengono sostiuiti nell'omonimo gruppo di {} nel testo
#
#esempio
#testo: "{a} e' piu grande di {b}"
#per sostituire a,b
#send_localized_reply(update, text_id, a="primo_ogg",b="secondo_ogg"):
def send_localized_reply(update, text_id, **optional_data):

    if update.message is None:
        print("[ERROR] unsupported update type! send_localized_reply only supports message updates!")

    update.message.reply_text( get_text(text_id, update.message.from_user).format(**optional_data) )