import numpy as np
from rich.console import Console

import User
import texts
import Add_matrixes


console = Console()
matrixes = {}


console.print(f"{texts.start}", style="red")

def main():
    console.print(f"{texts.man}", style="blue")
    comand = console.input("[bold green]=> ")

    match comand:
        case "0":
            Add_matrixes()

        case "3":
            pass

        case "h":
            pass

        case "q":
            exit()

        case _:
            console.print("[bold red] Команда не обнаружена")


while True:
    main()

