@echo off
if not exist .env (
    copy docker.env.example .env
)
docker-compose down
docker-compose up --build -d
timeout /t 10 /nobreak > nul
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py test_telegram 