import numpy as np
from rich.console import Console

import User
import texts


console = Console()
matrixes = {}


console.print(f"{texts.start}", style="red")

def main():
    console.print(f"{texts.man}", style="blue")
    comand = console.input("[bold green]=> ")

    match comand:
        case "3":
            pass

        case "h":
            pass

        case "q":
            exit()

        case _:
            console.print("[bold red] Команда не обнаружена")
    # matrix = User.get_matrix()
    # User.print_matrix(matrix)
    # determinant = np.linalg.det(matrix)
    # console.print(
    #     f"Определитель матрицы равен: [bold yellow]{determinant}\n",
    #     style="green"
    # )


while True:
    main()

