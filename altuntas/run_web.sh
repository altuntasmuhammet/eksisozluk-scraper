#!/bin/sh

python manage.py makemigrations;
python manage.py migrate;
if [ $APP_ENV == "PRODUCTION" ]
then
    python manage.py collectstatic --noinput;
    gunicorn altuntas.wsgi:application --bind 0.0.0.0:8000;
else
    python manage.py runserver 0.0.0.0:8000;
fi