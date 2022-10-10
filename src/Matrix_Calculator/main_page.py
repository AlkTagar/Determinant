import telebot
from rich.console import Console

import Config


bot = telebot.TeleBot(Config.TOKEN)
console = Console()


console.log("[bold green]START BOT")


@bot.message_handler(content_types=["text"])
def main_handler(message):
    match message.text:

        case "/start":
            bot.send_message(message.from_user.id, "Start bot")


bot.infinity_polling()
