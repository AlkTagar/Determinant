import numpy as np
from rich.console import Console


console = Console()


def search_roots(message):
    matrix = np.array(
        [[float(n) for n in i.split()] for i in message.text.split("\n")]
    ) # разбивает текст на строки и укладывает в матрицу

    matr_B = [[i] for i in matrix[:, -1]] # срез столбца "B"

    matr_inv_A = np.linalg.inv(
        np.delete(matrix, -1, 1)
    )

    matr_X = np.dot(matr_inv_A, matr_B)
    console.log(matr_X)

    return matr_X


def generate_system(message):
    pass
