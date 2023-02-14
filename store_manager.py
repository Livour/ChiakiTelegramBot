from json import load as json_load
from os.path import exists as does_path_exists
from telebot import TeleBot
from telebot.types import Message

# This is a module for managing the Key-Value store of the bot
# Included all CRUD functions
STORAGE_FILE = "store.json"


def initialize_all_store_commands(bot: TeleBot):
    initialize_commands_from_storage(bot)


def initialize_commands_from_storage(bot: TeleBot):
    # If the file doesn't exist, create an empty file
    if not does_path_exists(STORAGE_FILE):
        with open(STORAGE_FILE, "w"):
            pass
        return

    with open(STORAGE_FILE, "r") as items:
        data = json_load(items)

    for key, value in data.items():
        def handler(closure_value=value):
            def actual_handler(message: Message):
                bot.send_message(message.chat.id, closure_value)

            return actual_handler

        bot.message_handler(commands=[key])(handler())
