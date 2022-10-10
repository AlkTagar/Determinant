import numpy as np
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt


console = Console()


def get_matrix() -> np.ndarray:
    name = console.input("")
    order = int(Prompt.ask(
        "[bold magenta]Введите порядок матрицы",
        default="2"
    ))

    matrix = [[] for _ in range(order)]

    for i in matrix:
        nums = console.input(
            f"[blue]Введите через пробел элементы строки "+
            f"[bold green]{matrix.index(i)+1}[/]: "
        ).split()

        if len(nums) == order:
            for n in nums:
                i.append(float(n))
        else:
            console.print(
                f"[bold red]Количество элементов не соответствует "+
                "размерности матрицы"
            )
    return name, np.array(matrix)

