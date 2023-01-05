import telebot
import openai

openai.api_key = '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'

bot_api = '5905739184:AAEAZe-Hx_xpaI5ia0cIju-_1w0I4ccFu2E'

bot = telebot.TeleBot(bot_api)

print('Bot Started')
    
@bot.message_handler(commands = ['greet','start'])
def greet(message):
    msg = '''Tell Me Something\nI Will Convert Your Thoughts into an Image '''
    bot.send_message(message.chat.id, msg)
    
    
@bot.message_handler(content_types = 'text')
def response(message):
    image = openai.Image.create(
    prompt= message.text,
    n=1,
    size ='1024x1024') 
    img_url = (image)['data'][0]['url']
    bot.send_photo(message.chat.id, img_url)
    
bot.infinity_pooling(none_stop=True)

