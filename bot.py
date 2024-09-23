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




@bot.message_handler(content_types=['new_chat_members'])
def make_some(message):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)
















bot.infinity_polling()
