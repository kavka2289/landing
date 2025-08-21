from django.core.management.base import BaseCommand
from django.utils import timezone
import asyncio
from applications.telegram_service import telegram_notifier

class Command(BaseCommand):
    help = 'Тестирует отправку уведомления в Telegram'

    def handle(self, *args, **options):
        current_time = timezone.now().strftime('%d.%m.%Y %H:%M:%S')
        test_message = f"""
🔔 <b>Тестовое уведомление!</b>

✅ Telegram бот настроен правильно
⏰ Время: {current_time}
📱 Бот готов к работе!
        """.strip()

        # send_message is async, run it in a loop
        success = asyncio.run(telegram_notifier.send_message(test_message))

        if success:
            self.stdout.write('✅ Тестовое уведомление отправлено успешно!')
        else:
            self.stdout.write('❌ Ошибка отправки уведомления. Проверьте настройки.') 