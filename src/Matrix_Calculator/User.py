import numpy as np
import telebot
from rich.console import Console

import Systems
import Config


console = Console()
bot = telebot.TeleBot(Config.TOKEN)

def new_system(message): # TODO: norm math to math
    matrix = np.array(
        [[float(n) for n in i.split()] for i in message.text.split("\n")]
    ) # разбивает текст на строки и укладывает в матрицу

    roots = Systems.search_roots(matrix)

    for i in roots:
        bot.send_message(message.from_user.id, i)


def generate_system(message):
    n = int(message.text)

    matr, roots = Systems.generate_system(n)
    
    console.log(matr)
    console.log(roots)

    a = [" ".join([str(n) for n in i]) for i in matr]
    text = "\n".join(a)

    b = [" ".join([str(n) for n in i]) for i in roots]
    text_r = "\n".join(b)
    
    bot.send_message(message.from_user.id, text)
    bot.send_message(message.from_user.id, text_r)
    
