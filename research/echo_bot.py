import logging
import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv

# Load .env file
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create dispatcher (no bot here in v3)
dp = Dispatcher()


@dp.message(Command("start", "help"))
async def command_start_handler(message: Message):
    """
    Handles /start and /help commands
    """
    await message.reply(
        "Oh great… another human 😏\n"
        "Relax, I’m friendly.\n"
        "Ask your question before I get bored."
    )

@dp.message()
async def echo(message: Message):
    """
   This will return echo
    """
    await message.answer(message.text)

async def main():
    # Create bot inside async main
    bot = Bot(token=TELEGRAM_BOT_TOKEN)

    # Start polling
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
