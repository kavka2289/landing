# Настройка PostgreSQL

## Установка PostgreSQL

### macOS (через Homebrew)
```bash
# Установка PostgreSQL
brew install postgresql@14

# Запуск PostgreSQL
brew services start postgresql@14

# Создание базы данных
createdb landing_db

# Создание пользователя (опционально)
createuser -s postgres
```

### Ubuntu/Debian
```bash
# Установка PostgreSQL
sudo apt update
sudo apt install postgresql postgresql-contrib

# Запуск PostgreSQL
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Переключение на пользователя postgres
sudo -u postgres psql

# Создание базы данных и пользователя
CREATE DATABASE landing_db;
CREATE USER postgres WITH PASSWORD 'postgres';
GRANT ALL PRIVILEGES ON DATABASE landing_db TO postgres;
\q
```

## Настройка Django

После установки PostgreSQL измените настройки в `landing_site/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'landing_db',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Применение миграций

```bash
# Создание миграций
python manage.py makemigrations

# Применение миграций
python manage.py migrate
```

## Проверка подключения

```bash
# Проверка подключения к базе данных
python manage.py dbshell
```

## Полезные команды PostgreSQL

```sql
-- Подключение к базе данных
psql -d landing_db

-- Просмотр таблиц
\dt

-- Просмотр структуры таблицы
\d applications_application

-- Выполнение SQL запроса
SELECT * FROM applications_application;
``` 