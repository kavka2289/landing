from django.core.management.base import BaseCommand
import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

if not TELEGRAM_BOT_TOKEN:
    raise RuntimeError('TELEGRAM_BOT_TOKEN не найден в переменных окружения')

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('Бот работает!')

class Command(BaseCommand):
    help = 'Запуск асинхронного Telegram-бота через aiogram'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Запуск асинхронного Telegram-бота...'))
        asyncio.run(dp.start_polling(bot)) 