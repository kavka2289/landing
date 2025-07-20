#!/bin/bash

if [ ! -f .env ]; then
    cp docker.env.example .env
fi

docker-compose down
docker-compose up --build -d
sleep 10
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser --noinput || echo "Суперпользователь не создан"
docker-compose exec web python manage.py test_telegram 