import random

import numpy as np
from rich.console import Console


console = Console()


def search_roots(matrix):
    matr_B = [[i] for i in matrix[:, -1]] # срез столбца "B"

    matr_inv_A = np.linalg.inv(
        np.delete(matrix, -1, 1)
    )

    matr_X = np.dot(matr_inv_A, matr_B)
    console.log(matr_X)

    return matr_X


def generate_system(n: int):
    while True:
        matrix = np.array(
            [[random.randint(-10, 10) for _ in range(n + 1)] for _ in range(n)]
        )

        roots = search_roots(matrix)

        if all(i[0] == int(i[0]) for i in roots):
            return matrix, roots
