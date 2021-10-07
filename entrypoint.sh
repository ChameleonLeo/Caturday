#!/bin/sh

python manage.py makemigrations --noinput
python manage.py migrate
python manage.py collectstatic
exec "$@"