import aiohttp
import asyncio
import os
from django.conf import settings
import pytz
from asgiref.sync import async_to_sync

class TelegramNotifier:
    """Асинхронный сервис для отправки уведомлений в Telegram"""
    
    def __init__(self):
        self.bot_token = getattr(settings, 'TELEGRAM_BOT_TOKEN', None)
        self.chat_id = getattr(settings, 'TELEGRAM_CHAT_ID', None)
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}"
    
    async def send_message(self, message):
        """Асинхронная отправка сообщения в Telegram"""
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
            async with aiohttp.ClientSession() as session:
                async with session.post(url, data=data, timeout=10) as response:
                    response.raise_for_status()
                    return True
        except Exception as e:
            print(f"Ошибка отправки уведомления в Telegram: {e}")
            return False
    
    async def notify_new_application(self, application):
        """Асинхронное уведомление о новой заявке"""
        moscow_tz = pytz.timezone('Europe/Moscow')
        created_at_moscow = application.created_at.astimezone(moscow_tz)
        created_at_str = created_at_moscow.strftime('%d.%m.%Y %H:%M')
        message = f"""
🔔 <b>Новая заявка!</b>

👤 <b>Имя:</b> {application.name}
📧 <b>Email:</b> {application.email}
📱 <b>Телефон:</b> {application.phone}
📝 <b>Сообщение:</b> {application.message or 'Не указано'}
⏰ <b>Дата:</b> {created_at_str}
        """.strip()
        return await self.send_message(message)

    def notify_new_application_sync(self, application):
        """Синхронный вызов для совместимости с Django views"""
        return async_to_sync(self.notify_new_application)(application)

# Глобальный экземпляр
telegram_notifier = TelegramNotifier() 