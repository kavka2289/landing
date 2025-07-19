# Лендинг для заявок на Django

Современный лендинг для сбора заявок с базой данных, созданный на Django.

## Возможности

- ✅ Красивый современный дизайн
- ✅ Форма для сбора заявок
- ✅ AJAX отправка форм
- ✅ Админ-панель для управления заявками
- ✅ Адаптивный дизайн
- ✅ Валидация форм
- ✅ Уведомления об успешной отправке
- ✅ REST API с GET/POST запросами
- ✅ Swagger документация API
- ✅ Поддержка PostgreSQL
- ✅ Django REST Framework
- ✅ Статистика заявок через API
- ✅ Уведомления в Telegram о новых заявках

## Установка и запуск

### Вариант 1: Запуск через Docker (рекомендуется)

#### Быстрый запуск:
```bash
# На Windows:
docker-start.bat

# На Linux/Mac:
chmod +x docker-start.sh
./docker-start.sh
```

#### Ручной запуск:
```bash
# 1. Создайте файл .env из примера
cp docker.env.example .env

# 2. Запустите контейнеры
docker-compose up --build -d

# 3. Примените миграции
docker-compose exec web python manage.py migrate

# 4. Протестируйте Telegram бота
docker-compose exec web python manage.py test_telegram
```

### Вариант 2: Локальная установка

#### 1. Клонирование и настройка окружения

```bash
# Создание виртуального окружения
python3 -m venv venv

# Активация виртуального окружения
# На Windows:
venv\Scripts\activate
# На macOS/Linux:
source venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt

### 2. Настройка Telegram бота (опционально)

Для получения уведомлений о новых заявках в Telegram:

1. Создайте бота через @BotFather в Telegram
2. Получите токен бота и Chat ID
3. Создайте файл `.env` в корне проекта:
```
TELEGRAM_BOT_TOKEN=ваш_токен_бота
TELEGRAM_CHAT_ID=ваш_chat_id
```

Подробная инструкция: [TELEGRAM_SETUP.md](TELEGRAM_SETUP.md)
```

### 3. Настройка базы данных

```bash
# Создание миграций
python manage.py makemigrations

# Применение миграций
python manage.py migrate

# Создание суперпользователя (опционально)
python manage.py createsuperuser
```

### 4. Запуск сервера

```bash
python manage.py runserver
```

Сайт будет доступен по адресу: http://127.0.0.1:8000/

## Docker команды

```bash
# Запуск проекта
docker-compose up -d

# Остановка проекта
docker-compose down

# Просмотр логов
docker-compose logs web

# Перезапуск веб-сервера
docker-compose restart web

# Выполнение команд в контейнере
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py test_telegram
```

Админ-панель: http://127.0.0.1:8000/admin/

API Endpoints:
- GET /api/v1/applications/ - Список заявок
- GET /api/v1/applications/{id}/ - Детали заявки
- POST /api/v1/applications/create/ - Создание заявки
- GET /api/v1/applications/stats/ - Статистика заявок

Swagger документация: http://127.0.0.1:8000/swagger/

Тестирование API: http://127.0.0.1:8000/api-test/

### 5. Тестирование Telegram бота

```bash
# Отправка тестового уведомления
python manage.py test_telegram
```

## Структура проекта

```
landing_project/
├── applications/          # Основное приложение
│   ├── models.py         # Модель заявок
│   ├── views.py          # Представления
│   ├── forms.py          # Формы
│   ├── admin.py          # Админка
│   └── templates/        # Шаблоны
│       └── applications/
│           ├── base.html # Базовый шаблон
│           └── home.html # Главная страница
├── landing_site/         # Настройки проекта
│   ├── settings.py       # Настройки Django
│   └── urls.py           # Главные URL-маршруты
├── manage.py             # Управление Django
└── requirements.txt      # Зависимости
```

## Модель данных

### Application (Заявка)
- `name` - Имя клиента
- `email` - Email клиента
- `phone` - Телефон клиента
- `message` - Сообщение (необязательно)
- `created_at` - Дата создания заявки

## Технологии

- **Backend**: Django 5.2.4
- **API**: Django REST Framework 3.16.0
- **Documentation**: Swagger/OpenAPI (drf-yasg)
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 5.3.0
- **Icons**: Font Awesome 6.4.0
- **Database**: SQLite (по умолчанию) / PostgreSQL

## Настройка для продакшена

1. Измените `DEBUG = False` в `settings.py`
2. Настройте `ALLOWED_HOSTS`
3. Используйте PostgreSQL или MySQL вместо SQLite
4. Настройте статические файлы
5. Используйте HTTPS

## Лицензия

MIT License 