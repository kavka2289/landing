from django.core.management.base import BaseCommand
from applications.telegram_service import telegram_notifier

class Command(BaseCommand):
    help = 'Тестирует отправку уведомления в Telegram'

    def handle(self, *args, **options):
        test_message = """
🔔 <b>Тестовое уведомление!</b>

✅ Telegram бот настроен правильно
⏰ Время: {time}
📱 Бот готов к работе!
        """.strip()
        
        success = telegram_notifier.send_message(test_message)
        
        if success:
            self.stdout.write('✅ Тестовое уведомление отправлено успешно!')
        else:
            self.stdout.write('❌ Ошибка отправки уведомления. Проверьте настройки.') 