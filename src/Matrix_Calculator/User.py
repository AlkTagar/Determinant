import telebot
import rich

import Systems
import Config


bot = telebot.TeleBot(Config.TOKEN)

def new_system(message):
    roots = Systems.search_roots(message)

    for i in roots:
        bot.send_message(message.from_user.id, i)
