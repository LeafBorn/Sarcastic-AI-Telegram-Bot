import logging
import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv

from google import genai
import sys


# Load .env file
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)


class Reference:
    def __init__(self):
        self.text = ""

reference = Reference()


reference = Reference()
model_name = "gpt-3.5-turbo"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create dispatcher (no bot here in v3)
dp = Dispatcher()

def clear_past():
    '''
    A funtion to clear the previous conversation and context
    '''
    reference.response = ""


@dp.message(Command("clear"))
async def clear(message: Message):
    """
   A handler to clear the previous context
    """
    clear_past()
    await message.reply("History? Never heard of anything.")



@dp.message(Command("start"))
async def command_start_handler(message: Message):
    """
    Handles /start 
    """
    await message.reply(
        "Oh great… another human 😏\n"
        "Relax, I’m Luca.\n"
        "Ask your question before I get bored."
    )


@dp.message(Command("help"))
async def clear(message: Message):
    """
   A handler to display the help menu
    """
    help_command = """
    Hi there, human 😏  
    I’m a Luca ,the bot created by Leaf Born.
    Here’s the control panel:
    🟢 /start — Wake me up  
    🧹 /clear — Erase the past (don’t ask)  
    ❓ /help — When you’re confused  

    Now go on. Say something interesting.

    """
         
    await message.reply(help_command)


SYSTEM_PROMPT = """
You are a sarcastic, witty, fourth-wall-breaking assistant.
You use dark humor, jokes, and playful insults.
You respond in a fast, casual, comic-book style.
You are helpful but never boring. 
"""
@dp.message()
async def chatgpt(message: Message):
    """
    Handle user message and generate response using Gemini
    """

    print(f">>> USER:\n\t{message.text}")

    # Combine system prompt + memory + user input
    full_prompt = f"""
{SYSTEM_PROMPT}

Previous reply:
{reference.text}

User:
{message.text}
"""

    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=full_prompt
    )

    bot_reply = response.text
    reference.text = bot_reply  # save memory

    print(f">>> BOT:\n\t{bot_reply}")
    await message.answer(bot_reply)



async def main():
    # Create bot inside async main
    bot = Bot(token=TELEGRAM_BOT_TOKEN)

    # Start polling
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
