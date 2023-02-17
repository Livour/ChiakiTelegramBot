import json
from json import load as json_load
from os.path import exists as does_path_exists
from telebot import TeleBot
from telebot.types import Message

# This is a module for managing the Key-Value store of the bot
# Included all CRUD functions
STORAGE_FILE = "store.json"


# TODO add exceptions


def initialize_all_store_commands(bot: TeleBot):
    initialize_commands_from_storage(bot)

    @bot.message_handler(commands=["add_item"])
    def add_new_item(message: Message):
        bot.send_message(message.chat.id, "Great, what item do you want to add?")
        bot.register_next_step_handler(message, new_item_name)

    def new_item_name(message: Message):
        if is_stored(message.text):
            return bot.send_message(message.chat.id, "Oops, An item with the same name already exists")

        bot.send_message(message.chat.id, "Finally, give me the value you want to assign to that item")
        bot.register_next_step_handler(message, lambda value_message: new_item_value(value_message, message.text))

    def new_item_value(message: Message, name):
        add_to_storage(name, message.text)

        bot.message_handler(commands=[name])(
            lambda new_item_message: bot.send_message(new_item_message.chat.id, message.text))

        bot.send_message(message.chat.id, "The item has been added")




def initialize_commands_from_storage(bot: TeleBot):
    # If the file doesn't exist, create an empty file
    if not does_path_exists(STORAGE_FILE):
        with open(STORAGE_FILE, "w"):
            pass
        return

    data = get_all_storage()

    for key, value in data.items():
        def handler(closure_value=value):
            def actual_handler(message: Message):
                bot.send_message(message.chat.id, closure_value)

            return actual_handler

        bot.message_handler(commands=[key])(handler())


def is_stored(text):
    data = get_all_storage()
    return text in data.keys()


def get_all_storage() -> dict:
    with open(STORAGE_FILE, "r") as items:
        return json_load(items)


def add_to_storage(key, value):
    data = get_all_storage()
    data[key] = value
    with open(STORAGE_FILE, "w") as items:
        json.dump(data, items)
