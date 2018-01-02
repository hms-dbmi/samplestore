#!/bin/bash

FIRST_ADMIN_EMAIL="natebessa@gmail.com"

cd /app/

if [ ! -d static ]; then
  mkdir static
fi

python manage.py migrate
python manage.py collectstatic --no-input
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('$FIRST_ADMIN_EMAIL', '$FIRST_ADMIN_EMAIL', '')" || echo "Super User already exists."

/etc/init.d/nginx restart

chown -R www-data:www-data /app

gunicorn samplestore.wsgi:application -b 0.0.0.0:8002  --user=www-data --group=www-data