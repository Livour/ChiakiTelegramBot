from json import load as json_load
from os.path import exists as does_path_exists
from telebot import TeleBot
from telebot.types import Message

STORAGE_FILE = "url.json"


def initialize_url_commands(bot: TeleBot):
    # If the file doesn't exist, create an empty file
    if not does_path_exists(STORAGE_FILE):
        with open(STORAGE_FILE, "w"):
            pass
        return

    with open(STORAGE_FILE, "r") as urls:
        data = json_load(urls)

    for key, value in data.items():
        def handler(closure_value=value):
            def actual_handler(message: Message):
                bot.send_message(message.chat.id, closure_value)

            return actual_handler

        bot.message_handler(commands=[key])(handler())
