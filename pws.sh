#!/bin/sh

# Collect static files
python manage.py collectstatic --noinput

if [ $? -eq 0 ]; then
    python manage.py runserver 0.0.0.0:8000
else
    # Collectstatic failed
    echo "Collectstatic failed. Exiting."
    exit 1
fi