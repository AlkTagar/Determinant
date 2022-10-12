from rich import style
import telebot
from rich.console import Console

import Config
import Systems
import texts


bot = telebot.TeleBot(Config.TOKEN)
console = Console()


console.log("START BOT", style="bold green")


@bot.message_handler()
def main_handler(message):
    match message.text:

        case "/start":
            bot.send_message(message.from_user.id, texts.start)
            console.log("get \"start\"", style="italic cyan")

        case "/new_system":
            bot.send_message(message.from_user.id, texts.system)
            console.log("new system", style="italic blue")

        case _:
            bot.send_message(message.from_user.id, "?")
            console.log("unknown message", style="italic yellow")


bot.infinity_polling()

