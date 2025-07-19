# 🐳 Руководство по Docker

## ✅ Проект успешно запущен!

Ваш лендинг с Telegram уведомлениями теперь работает в Docker контейнерах.

## 🌐 Доступные адреса

- **Главная страница**: http://localhost:8000
- **Админ-панель**: http://localhost:8000/admin
  - Логин: `admin`
  - Пароль: `admin` (по умолчанию)
- **API документация**: http://localhost:8000/swagger
- **Тестирование API**: http://localhost:8000/api-test

## 📱 Telegram уведомления

✅ **Работает!** Тестовое уведомление отправлено успешно.

При каждой новой заявке вы получите уведомление в Telegram с информацией о клиенте.

## 🐳 Docker команды

### Основные команды

```bash
# Запуск проекта
docker-compose up -d

# Остановка проекта
docker-compose down

# Перезапуск
docker-compose restart

# Просмотр логов
docker-compose logs web
docker-compose logs db

# Просмотр статуса контейнеров
docker-compose ps
```

### Выполнение команд в контейнере

```bash
# Применение миграций
docker-compose exec web python manage.py migrate

# Создание суперпользователя
docker-compose exec web python manage.py createsuperuser

# Тестирование Telegram бота
docker-compose exec web python manage.py test_telegram

# Создание миграций
docker-compose exec web python manage.py makemigrations

# Сбор статических файлов
docker-compose exec web python manage.py collectstatic
```

### Управление данными

```bash
# Резервное копирование базы данных
docker-compose exec db pg_dump -U postgres landing_db > backup.sql

# Восстановление базы данных
docker-compose exec -T db psql -U postgres landing_db < backup.sql

# Очистка всех данных (осторожно!)
docker-compose down -v
```

## 🔧 Настройка

### Изменение настроек Telegram

1. Отредактируйте файл `.env`:
```env
TELEGRAM_BOT_TOKEN=ваш_новый_токен
TELEGRAM_CHAT_ID=ваш_новый_chat_id
```

2. Перезапустите контейнеры:
```bash
docker-compose restart web
```

### Изменение портов

Отредактируйте `docker-compose.yml`:
```yaml
ports:
  - "8080:8000"  # Изменить 8000 на 8080
```

## 🚨 Устранение проблем

### Контейнеры не запускаются

```bash
# Проверьте логи
docker-compose logs

# Пересоберите образы
docker-compose up --build -d
```

### База данных недоступна

```bash
# Проверьте статус PostgreSQL
docker-compose exec db pg_isready -U postgres

# Перезапустите базу данных
docker-compose restart db
```

### Telegram уведомления не работают

```bash
# Проверьте настройки
docker-compose exec web python manage.py test_telegram

# Проверьте переменные окружения
docker-compose exec web env | grep TELEGRAM
```

### Очистка Docker

```bash
# Удалить неиспользуемые образы
docker image prune

# Удалить неиспользуемые контейнеры
docker container prune

# Полная очистка
docker system prune -a
```

## 📊 Мониторинг

### Просмотр ресурсов

```bash
# Использование ресурсов контейнерами
docker stats

# Информация о контейнерах
docker-compose ps
```

### Логи в реальном времени

```bash
# Логи веб-сервера
docker-compose logs -f web

# Логи базы данных
docker-compose logs -f db
```

## 🔒 Безопасность

### Для продакшена

1. Измените пароли в `.env`
2. Настройте HTTPS
3. Используйте секреты Docker
4. Ограничьте доступ к портам

### Переменные окружения

Все чувствительные данные хранятся в файле `.env`:
- Токены Telegram
- Пароли базы данных
- Секретные ключи Django

## 📝 Полезные советы

1. **Быстрый перезапуск**: `docker-compose restart web`
2. **Просмотр логов**: `docker-compose logs -f web`
3. **Обновление кода**: Просто перезапустите контейнеры
4. **Резервное копирование**: Регулярно делайте бэкапы базы данных

## 🎉 Готово!

Ваш проект полностью настроен и готов к работе! 

При возникновении вопросов обращайтесь к основной документации: [README.md](README.md) 