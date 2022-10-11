import telebot
from rich.console import Console

import Config
import Systems


bot = telebot.TeleBot(Config.TOKEN)
console = Console()


console.log("[bold green]START BOT")


@bot.message_handler(content_types=["text"])
def main_handler(message):
    match message.text:

        case "/start":
            bot.send_message(message.from_user.id, "Start bot")
            console.log("[cyan]get \"start\"")

        case "/new_system":
            pass


bot.infinity_polling()
