import telebot
from rich.console import Console

import Config


bot = telebot.TeleBot(Config.TOKEN)
console = Console()


console.log("[bold green]START BOT")


@bot.message_handler(content_types=["text"])
def main_handler():
    pass
