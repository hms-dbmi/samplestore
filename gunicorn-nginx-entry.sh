#!/bin/bash

MYSQL_USERNAME=$(aws ssm get-parameters --names $PS_PATH.mysql_username --with-decryption --region us-east-1 | jq -r '.Parameters[].Value')
MYSQL_PASSWORD=$(aws ssm get-parameters --names $PS_PATH.mysql_pw --with-decryption --region us-east-1 | jq -r '.Parameters[].Value')
MYSQL_HOST=$(aws ssm get-parameters --names $PS_PATH.mysql_host --with-decryption --region us-east-1 | jq -r '.Parameters[].Value')
MYSQL_PORT=$(aws ssm get-parameters --names $PS_PATH.mysql_port --with-decryption --region us-east-1 | jq -r '.Parameters[].Value')

DJANGO_SECRET=$(aws ssm get-parameters --names $PS_PATH.django_secret --with-decryption --region us-east-1 | jq -r '.Parameters[].Value')

export MYSQL_USERNAME=$MYSQL_USERNAME
export MYSQL_PASSWORD=$MYSQL_PASSWORD
export MYSQL_HOST=$MYSQL_HOST
export MYSQL_PORT=$MYSQL_PORT

export SECRET_KEY=$DJANGO_SECRET

FIRST_ADMIN_EMAIL="natebessa@gmail.com"

cd /app/

if [ ! -d static ]; then
  mkdir static
fi

python manage.py migrate
python manage.py collectstatic --no-input
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('$FIRST_ADMIN_EMAIL', '$FIRST_ADMIN_EMAIL', '')" || echo "Super User already exists."
python manage.py loaddata initial_data

/etc/init.d/nginx restart

chown -R www-data:www-data /app

gunicorn samplestore.wsgi:application -b 0.0.0.0:8001  --user=www-data --group=www-data