from os import getenv
from dotenv import load_dotenv
from telebot import TeleBot
from telebot.types import Message

from url_manager import initialize_url_commands


def main():
    load_dotenv()
    bot_token = getenv('bot_token')

    bot = TeleBot(bot_token)

    @bot.message_handler(commands=['start', 'hello', "help"])
    def send_help_details(message: Message):
        bot.send_message(message.chat.id, "*Hola I'm Chiaki*\n"
                                          "I am a quality of life assistant\n\n"
                                          "I can quickly manage your URLS and help you use MAL more efficiently\n\n"
                                          "maybe I will have more features on the future 🤷‍♂", parse_mode="MarkdownV2")

    initialize_url_commands(bot)

    print('----------------------\n'
          'Chiaki is now running\n'
          '----------------------')

    bot.polling()


if __name__ == "__main__":
    main()
