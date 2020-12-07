#!/bin/bash
# Apply database migrations
echo "Apply database migrations"
./manage.py migrate

# Creating superuser
./manage.py shell -c "from django.contrib.auth.models import User; import os; User.objects.create_superuser(os.getenv('DJANGO_USER'), os.getenv('DJANGO_EMAIL'), os.getenv('DJANGO_PASSWORD'))"

# Start server
echo "Starting server"
./manage.py runserver 0.0.0.0:8000