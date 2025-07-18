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

## Установка и запуск

### 1. Клонирование и настройка окружения

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
```

### 2. Настройка базы данных

```bash
# Создание миграций
python manage.py makemigrations

# Применение миграций
python manage.py migrate

# Создание суперпользователя (опционально)
python manage.py createsuperuser
```

### 3. Запуск сервера

```bash
python manage.py runserver
```

Сайт будет доступен по адресу: http://127.0.0.1:8000/

Админ-панель: http://127.0.0.1:8000/admin/

API Endpoints:
- GET /api/v1/applications/ - Список заявок
- GET /api/v1/applications/{id}/ - Детали заявки
- POST /api/v1/applications/create/ - Создание заявки
- GET /api/v1/applications/stats/ - Статистика заявок

Swagger документация: http://127.0.0.1:8000/swagger/

Тестирование API: http://127.0.0.1:8000/api-test/

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