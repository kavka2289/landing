import requests
import os
from django.conf import settings

class TelegramNotifier:
    """Сервис для отправки уведомлений в Telegram"""
    
    def __init__(self):
        self.bot_token = getattr(settings, 'TELEGRAM_BOT_TOKEN', None)
        self.chat_id = getattr(settings, 'TELEGRAM_CHAT_ID', None)
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}"
    
    def send_message(self, message):
        """Отправка сообщения в Telegram"""
        if not self.bot_token or not self.chat_id:
            print("Telegram настройки не найдены. Уведомление не отправлено.")
            return False
        
        try:
            url = f"{self.base_url}/sendMessage"
            data = {
                'chat_id': self.chat_id,
                'text': message,
                'parse_mode': 'HTML'
            }
            response = requests.post(url, data=data, timeout=10)
            response.raise_for_status()
            return True
        except Exception as e:
            print(f"Ошибка отправки уведомления в Telegram: {e}")
            return False
    
    def notify_new_application(self, application):
        """Уведомление о новой заявке"""
        message = f"""
🔔 <b>Новая заявка!</b>

👤 <b>Имя:</b> {application.name}
📧 <b>Email:</b> {application.email}
📱 <b>Телефон:</b> {application.phone}
📝 <b>Сообщение:</b> {application.message or 'Не указано'}
⏰ <b>Дата:</b> {application.created_at.strftime('%d.%m.%Y %H:%M')}
        """.strip()
        
        return self.send_message(message)

# Создаем глобальный экземпляр
telegram_notifier = TelegramNotifier() 