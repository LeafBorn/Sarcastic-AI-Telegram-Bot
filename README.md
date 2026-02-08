# Sarcastic-AI-Telegram-Bot
Chat with an intelligent assistant powered by Gemini AI and built with Aiogram. Ask questions, get instant answers, and boost your productivity right inside Telegram.

## 🚀 Features

💬 AI-powered chat using Google Gemini

⚡ Fast & asynchronous bot built with Aiogram

🔒 Secure token and API key handling via environment variables

🧠 Context-aware responses

🛠 Easy to extend with new commands and features

📦 Clean and modular project structure

## PROJECT STRUCTURE
```
gemini-telegram-bot/
│
├── bot.py                # Main bot entry point
├── config.py             # Configuration and environment variables
├── handlers/
│   └── chat.py           # Message handlers
├── services/
│   └── gemini.py         # Gemini AI integration
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variable template
└── README.md             # Project documentation
```


## 🧠 How It Works

User sends a message to the Telegram bot

Aiogram handles the update asynchronously

## 🧰 Tech Stack

Python 3.9+

- Aiogram – Telegram Bot Framework

- Google Gemini API – AI model

- asyncio

- python-dotenv – Environment variable management

- Message is forwarded to Gemini AI

- Gemini generates a response

- Bot sends the response back to the user
