import numpy as np
from rich.console import Console

import User


console = Console()


def main():
    matrix = User.get_matrix()
    User.print_matrix(matrix)
    determinant = np.linalg.det(matrix)
    console.print(
        f"Определитель матрицы равен: [bold yellow]{determinant}\n",
        style="green"
    )


if __name__ == "__main__":
    while True:
        main()

