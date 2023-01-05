import telebot
import openai

openai.api_key = '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'

bot_api = '5905739184:AAEAZe-Hx_xpaI5ia0cIju-_1w0I4ccFu2E'

bot = telebot.TeleBot(bot_api)

print('Bot Started')
    
@bot.message_handler(commands = ['greet','start'])
def greet(message):
    msg = ''' Ask Me Something\nI Will Convert Them into Image '''
    bot.send_message(message.chat.id, msg)
    
    
@bot.message_handler(content_types = 'text')
def response(message):
    image = openai.Image.create(
    prompt= message.text,
    n=3,
    size ='1024x1024') 
    img_url = (image)['data'][0]['url']
    bot.send_photo(message.chat.id, img_url)
    
bot.polling(none_stop=True)

