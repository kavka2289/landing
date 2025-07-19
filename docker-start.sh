#!/bin/bash

echo "🚀 Запуск проекта через Docker..."

# Проверяем, существует ли файл .env
if [ ! -f .env ]; then
    echo "📝 Создаем файл .env из примера..."
    cp docker.env.example .env
    echo "✅ Файл .env создан!"
fi

# Останавливаем существующие контейнеры
echo "🛑 Останавливаем существующие контейнеры..."
docker-compose down

# Собираем и запускаем контейнеры
echo "🔨 Собираем и запускаем контейнеры..."
docker-compose up --build -d

# Ждем, пока база данных запустится
echo "⏳ Ждем запуска базы данных..."
sleep 10

# Применяем миграции
echo "📊 Применяем миграции..."
docker-compose exec web python manage.py migrate

# Создаем суперпользователя (опционально)
echo "👤 Создание суперпользователя..."
echo "Введите данные для суперпользователя (или нажмите Enter для пропуска):"
docker-compose exec web python manage.py createsuperuser --noinput || echo "Суперпользователь не создан"

# Тестируем Telegram бота
echo "📱 Тестируем Telegram бота..."
docker-compose exec web python manage.py test_telegram

echo "✅ Проект запущен!"
echo "🌐 Сайт доступен по адресу: http://localhost:8000"
echo "📊 Админ-панель: http://localhost:8000/admin"
echo "📚 API документация: http://localhost:8000/swagger"
echo "🧪 Тестирование API: http://localhost:8000/api-test"

echo ""
echo "📋 Полезные команды:"
echo "  docker-compose logs web    - просмотр логов"
echo "  docker-compose down        - остановка проекта"
echo "  docker-compose restart web - перезапуск веб-сервера" 