from telebot import TeleBot


def remove_handler(bot: TeleBot, command):
    for handler in bot.message_handlers:
        if command in handler["filters"]["commands"]:
            return bot.message_handlers.remove(handler)
