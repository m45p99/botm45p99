import telebot 
from config import TOKEN
from telebot.types import Message
from random import choice

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def hi_cmd(message: Message):
    bot.reply_to(message,"hi")


@bot.message_handler(commands=["info"])
def info_cmd(message: Message):
    bot.reply_to(message,"info")



from random import choice

@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = choice(["ОРЕЛ", "РЕШКА"])
    bot.reply_to(message, coin)





















bot.infinity_polling()