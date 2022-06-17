#!/bin/sh

python manage.py migrate --no-input 
python manage.py collectstatic --no-input

gunicorn --chdir youtu6e youtu6e.wsgi:application --bind 0.0.0.0:8000