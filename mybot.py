import telebot
import openai

openai.api_key = # Your OpenAI API key

bot_api = # Your Telegram Bot key

bot = telebot.TeleBot(bot_api)

print('Bot Started...')

@bot.message_handler(commands= ['answer_me'])
def chatbot(message):
    name = f"{message.from_user.first_name} {message.from_user.last_name}"
    msg = f"Hi {name}!\nEnter The Question You Want To Ask."
    bot.send_message(message.chat.id, msg)
    @bot.message_handler(content_types='text')
    def gpt(message):
            text = openai.Completion.create(
            model="text-davinci-003",
            prompt= message.text,
            temperature=0.7,
            max_tokens= 256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.0)
            response= (text)["choices"][0]['text'][2:]
            bot.send_message(message.chat.id, response)
        
bot.polling()
    

    
