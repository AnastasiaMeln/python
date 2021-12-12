class Cells:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return Cells(self.quantity + other.quantity)

    def __sub__(self, other):
            return Cells(self.quantity - other.quantity)

    def __mul__(self, other):
        return Cells(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cells(round(self.quantity / other.quantity))

    def __str__(self):
        if self.quantity >= 0:
            return f"Итого клеток - {self.quantity * '*'}"
        else:
            return 'Разность клеток меньше нуля'

def make_order(rows, nums):
    return '\n'.join(['*' * rows for _ in range(nums // rows)]) + '\n' + '*' * (nums % rows)

cell1 = Cells(10)
cell2 = Cells(5)

print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print(make_order(5, 15))

