FROM python:2.7-slim

RUN pip install pipenv

#copia i file necessari al bot
WORKDIR /bot

ADD src src
ADD Pipfile Pipfile
ADD Pipfile.lock Pipfile.lock
RUN pipenv install --system

#imposta le variabili del bot
ENV TOKEN telegram_token
ENV PORT 6666
ENV APP_LINK test
ENV DEBUG false

#esponi porta
EXPOSE 6666

#importa il comando di avvio
CMD ["python", "src/main.py"]