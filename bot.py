import requests
from aiogram import Bot, Dispatcher, executor, types
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}