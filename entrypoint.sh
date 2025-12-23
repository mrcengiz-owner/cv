#!/bin/sh

# Exit on error
set -e

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run gunicorn
echo "Starting Gunicorn..."
exec gunicorn cv_project.wsgi:application --bind 0.0.0.0:8000
