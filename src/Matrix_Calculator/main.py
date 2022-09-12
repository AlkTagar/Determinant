import copy

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt


console = Console()


class Matrix:

    def __init__(self):
        """Constructor"""

        order = int(Prompt.ask(
            "[bold magenta]Введите порядок матрицы",
            default="2"
        ))
        self.matrix = [[] for _ in range(order)]

        for i in self.matrix:
            nums = console.input(
                f"[blue]Введите через пробел элементы строки "+
                f"[bold green]{self.matrix.index(i)+1}[/]: "
            ).split()

            if len(nums) == order:
                for n in nums:
                    i.append(float(n))
            else:
                console.print(
                    f"[bold red]Количество элементов не соответствует "+
                    "размерности матрицы"
                )

    def print(self):
        """
        Выводит на экран матрицу в виде таблицы
        """
        table = Table(
            show_lines=True,
            show_header=False,
            show_footer=False,
            show_edge=False
        )

        str_matrix = [[str(n) for n in i] for i in self.matrix]

        for i in range(len(str_matrix)):
            table.add_column(
                justify="center",
                vertical="middle"
            )

        for i in str_matrix:
            table.add_row(*i)

        console.print(table)


    def rm_row(self, index):
        self.matrix.pop(index)


    def rm_column(self, index):
        for i in self.matrix:
            i.pop(index)


    def minor(self, y, x):
        s = copy.deepcopy(self)
        s.rm_row(y)
        s.rm_column(x)
        return s.search_determinant()


    def search_determinant(self):
        """
        out: Определитель указанной матрицы
        """
        m = self.matrix
        match len(m):
            case 2:
                self.determinant = (
                    (m[0][0] * m[1][1])-
                    (m[0][1] * m[1][0])
                )
                return self.determinant

            case _:
                self.determinant = 0
                for i in m[0]:
                    self.determinant += i * (
                        (-1)**(2+m[0].index(i))*
                        self.minor(0, m[0].index(i))
                    )
                return self.determinant


mat = Matrix()
mat.print()
determinant = mat.search_determinant()
console.print(
    f"Определитель матрицы равен: [bold yellow]{determinant}",
    style="green"
)

