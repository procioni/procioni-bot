#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################################################
#
#    EmyTagBot
#    A Telegram bot meant to create user-based hashtags contents with text, images, audios, sticker, videos.
#    Copyright (C) 2018  RickyCorte
#    https://github.com/rickycorte
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
    
    print("Check complete, starting bot")