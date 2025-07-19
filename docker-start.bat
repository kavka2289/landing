@echo off
echo 🚀 Запуск проекта через Docker...

REM Проверяем, существует ли файл .env
if not exist .env (
    echo 📝 Создаем файл .env из примера...
    copy docker.env.example .env
    echo ✅ Файл .env создан!
)

REM Останавливаем существующие контейнеры
echo 🛑 Останавливаем существующие контейнеры...
docker-compose down

REM Собираем и запускаем контейнеры
echo 🔨 Собираем и запускаем контейнеры...
docker-compose up --build -d

REM Ждем, пока база данных запустится
echo ⏳ Ждем запуска базы данных...
timeout /t 10 /nobreak > nul

REM Применяем миграции
echo 📊 Применяем миграции...
docker-compose exec web python manage.py migrate

REM Тестируем Telegram бота
echo 📱 Тестируем Telegram бота...
docker-compose exec web python manage.py test_telegram

echo ✅ Проект запущен!
echo 🌐 Сайт доступен по адресу: http://localhost:8000
echo 📊 Админ-панель: http://localhost:8000/admin
echo 📚 API документация: http://localhost:8000/swagger
echo 🧪 Тестирование API: http://localhost:8000/api-test

echo.
echo 📋 Полезные команды:
echo   docker-compose logs web    - просмотр логов
echo   docker-compose down        - остановка проекта
echo   docker-compose restart web - перезапуск веб-сервера

pause 