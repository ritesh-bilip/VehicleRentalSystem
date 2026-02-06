#!/usr/bin/env bash
pip install -r requirements.txt
pip install psycopg2-binary
python manage.py collectstatic --noinput
python manage.py migrate
