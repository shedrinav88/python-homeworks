class Cell:
    def __init__(self, cell_num):
        self.cell_num = cell_num

    def __str__(self):
        return f'A cell with {self.cell_num} cells'

    def __add__(self, other):
        return Cell(self.cell_num + other.cell_num)

    def __sub__(self, other):
        if self.cell_num - other.cell_num > 0:
            return Cell(self.cell_num - other.cell_num)
        else:
            return "The result of subtraction of two cells can't be a negative"

    def __mul__(self, other):
        return Cell(self.cell_num * other.cell_num)

    def __truediv__(self, other):
        return Cell(self.cell_num // other.cell_num)

    def make_order(self, number):
        rows = self.cell_num // number
        last_row = self.cell_num % number

        return ('*' * number + '\n') * rows + '*' * last_row


cell_1 = Cell(6)
print(cell_1)
cell_2 = Cell(8)
print(cell_2)
cell_3 = cell_1 + cell_2
print(cell_3)
cell_4 = cell_3 - cell_2
print(cell_4)
cell_5 = cell_2 - cell_3
print(cell_5)
cell_6 = cell_1 * cell_3
print(cell_6)
cell_7 = cell_6 / cell_2
print(cell_7)
print(f'cell_6 in order:\n{cell_6.make_order(19)}')

