import os
import logging
from aiogram import Bot, Dispatcher, executor, types

from book import Book
from author import Author
from review import Review
from user import User

API_TOKEN = os.getenv('API_TELEGRAM_BOT')
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
db = Dispatcher(bot)


def main():

    @db.message_handler(commands=['start', 'help'])
    async def send_welcome(message: types.Message):
        """
        This handler will be called when user sends `/start` or `/help`
        command
        """
        await message.reply('Hi!\nI\'m EchoBot!\nPowered by aiogram.')

    @db.message_handler()
    async def echo(message: types.Message):
        await message.answer(message.text)


if __name__ == '__main__':
    main()
    executor.start_polling(db, skip_updates=True)
