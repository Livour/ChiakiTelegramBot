from os import getenv
from dotenv import load_dotenv
from telebot import TeleBot
from telebot.types import Message

load_dotenv()
BOT_TOKEN = getenv('BOT_TOKEN')

bot = TeleBot(BOT_TOKEN, parse_mode="MarkdownV2")


@bot.message_handler(commands=['start', 'hello', "help"])
def send_welcome(message: Message):
    bot.send_message(message.chat.id, "*Hola I'm Chiaki*\n"
                                      "I am a quality of life assistant\n\n"
                                      "I can quickly manage your URLS and help you use MAL more efficiently\n\n"
                                      "maybe I will have more features on the future 🤷‍♂")


print('----------------------\n'
      'Chiaki is now running\n'
      '----------------------')

bot.polling()
