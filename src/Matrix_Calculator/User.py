import numpy as np
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt


console = Console()


def get_matrix() -> np.ndarray:
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
    return np.array(matrix)


def print_matrix(matrix: np.ndarray) -> None:
    """
    Выводит на экран матрицу в виде таблицы
    """
    table = Table(
        show_lines=True,
        show_header=False,
        show_footer=False,
        show_edge=False
    )

    str_matrix = [[str(n) for n in i] for i in matrix]

    for i in range(len(str_matrix)):
        table.add_column(
            justify="center",
            vertical="middle"
        )

    for i in str_matrix:
        table.add_row(*i)

    console.print(table)

