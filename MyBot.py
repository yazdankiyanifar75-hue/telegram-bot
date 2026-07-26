import telebot
import os

TOKEN = os.getenv("TOKEN")  # از Railway می‌خونه

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "ربات روشنه ✅")

@bot.message_handler(func=lambda message: message.text == "سلام")
def reply_salame(message):
    bot.reply_to(message, "سلام سورنا 🌹")

bot.infinity_polling()
