import copy

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

from Classes import Matrix


console = Console()


mat = Matrix()
mat.print()
determinant = mat.search_determinant()
console.print(
    f"Определитель матрицы равен: [bold yellow]{determinant}",
    style="green"
)

