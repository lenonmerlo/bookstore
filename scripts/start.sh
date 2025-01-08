#!/usr/bin/env bash

set -ex

python manage.py makemigrations
gunicorn bookstore.wsgi:application --bind "0.0.0.0:8000"
