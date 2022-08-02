import telebot
from time import sleep
import random
import json

from telebot import types


TOKEN = '2043280308:AAGfz7pA6Oc9510Dp4b7VSMLXTKwZqoheAg'
bot = telebot.TeleBot(TOKEN)

#клавиатура
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Новий комплімент❤️")

markup.add(item1)

#команда сттарт
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привіт Юлічка!👋 Я створив цього бота щоб він говорив тобі компліменти💕', reply_markup=markup)

with open('compliments.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


@bot.message_handler(content_types=['text'])
def lalala(message):
    random_compliment = random.choice(data['compliments'])
    if message.chat.type == 'private':
        if message.text == 'Новий комплімент❤️':
            bot.send_message(message.chat.id, random_compliment)



#текст
@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, 'Привет')

bot.polling()
