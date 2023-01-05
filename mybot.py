import telebot
import openai
from urllib.request import urlopen
from PIL import Image
from io import BytesIO
from api_key import Api_Key
from random import randint


bot = telebot.TeleBot('5905739184:AAEAZe-Hx_xpaI5ia0cIju-_1w0I4ccFu2E')

@bot.message_handler(commands = ['greet','start'])
def greet(message):
    msg = ''' Hello, how are you? '''
    bot.send_message(message.chat.id, msg)