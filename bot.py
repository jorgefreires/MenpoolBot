import os
import telebot
import requests

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hola'])
def send_welcome(message):
    bot.reply_to(message, "Hola!!! Me llamo MenpoolBot y estoy aquí para ayudarte a conocer el estado de la Menpool de Bitcoin y avisarte cuando las fees esten bajas")

@bot.message_handler(commands=['fees'])
def send_welcome(message):
    response = requests.request("GET", "https://mempool.space/api/v1/fees/mempool-blocks")
    medianFee = response.json()[0]['medianFee']
    bot.reply_to(message, f'Las mediana de las fees para el siguiente bloque es de {medianFee}')

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()