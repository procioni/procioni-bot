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

import os
from pymongo import MongoClient

def check():
    #controlla che tutte le variabili necessarie siano state settate altrimenti chiudi il bot
    print("Checking required variables...")

    crit_vars = ['TOKEN','PORT','APP_LINK']
    for itm in crit_vars:
        CURR_VAR = os.environ.get(itm, None)
        if CURR_VAR is None:
            print("[Critical] Missing " + itm + " var value. Closing bot.")
            exit(1)

    #controlla che le variabili accessorie siano state settate altrimenti printa un avviso
    print("Checking other variables...")

    misc_vars = []
    for itm in misc_vars:
        CURR_VAR = os.environ.get(itm, None)
        if CURR_VAR is None:
            print("[Settings] Missing " + itm + " var value.")

    #controlla che sia possibile connetersi a mongodb
    print("Checking database...")

    try:
        #controlla che mongodb vada
        client = MongoClient( os.environ.get('MONGO_URI', 'error'), serverSelectionTimeoutMS=100 )
        res = client.server_info()
    except:
        print("[Critical] Can't connect to mongodb. Check it is up and running. Closing bot.")
        exit(2)
    
    
    print("Check complete, starting bot")