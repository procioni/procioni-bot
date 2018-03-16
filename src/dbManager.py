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

from pymongo import MongoClient
import os

client = MongoClient( os.environ.get('MONGO_URI', 'error') )
db = client[ os.environ.get('DB_NAME', 'procione_furioso') ] 

#controlla se esiste utente
def exist_user(telegramID):
    cursor = db.users.find({ "telegramID": telegramID })
    if cursor.count() > 0:
        return True
    else:
        return False

#aggiunge un utente al db se manca
def create_user(name, telegramID):
    db.users.update_one(
            {
                "telegramID": telegramID
            },
            {"$set":
                {
                    "name": name,
                    "telegramID": telegramID
                }
            }
        , upsert=True) #aggiunge o aggiorna un utente

