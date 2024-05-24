# Imports
import os
import telebot
import requests
from telebot.types import BotCommand

# Adding the bot API Token
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)


# List of commands for the menu
commands = [
    BotCommand(command='fees', description='Obtén el valor mediano de las fees para el siguiente bloque')
]
bot.set_my_commands(commands)

# Functions

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hola!!! Me llamo MenpoolBot y estoy aquí para ayudarte a conocer el estado de la Menpool de Bitcoin y avisarte cuando las fees esten bajas")

@bot.message_handler(commands=['fees'])
def send_welcome(message):
    response = requests.request("GET", "https://mempool.space/api/v1/fees/mempool-blocks")
    medianFee = response.json()[0]['medianFee']
    bot.send_message(message.chat.id, f'Las mediana de las fees para el siguiente bloque es de {medianFee}')

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


# Starting the bot
bot.infinity_polling()