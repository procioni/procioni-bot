# procioni-bot

Solo un bot procione creato per divertimento

## Features
* Nulla

## Requisiti
* Python 2.7
* PipEnv

## Dipendenze
* python-telegram-bot
* pymongo

## Variabili

[REQUIRED] `TOKEN`: telegram bot token

[REQUIRED] `PORT`: porta da usare con il webhook

[REQUIRED] `APP_LINK`: link da passare a telegram come webhook (no token, viene aggiunto in automatico)

[REQUIRED] `MONGO_URI`: url di connesione a mongodb

[REQUIRED] `DB_NAME`: nome del database da usare

`DEBUG`: true per il polling

## Avvia il bot
Per eseguire il bot sulla tua macchina:

`pipenv install`

`pipenv shell`

`python src/main.py`


Se vuoi usare docker esegui:

`docker build -t procione .`

`docker run -p 80:6666 -d procione`
