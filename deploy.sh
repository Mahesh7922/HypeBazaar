#!/bin/bash

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Check for any deployment issues
python manage.py check --deploy

# Start Gunicorn
gunicorn ecommerce.wsgi:application