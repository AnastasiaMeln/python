class Textil:
    def __init__(self, size, height):
        self.size = size
        self.height = height

class Coat(Textil):
    def __init__(self, size):
        self.size = size
    @property
    def get_square_coat(self):
        return self.size / 6.5 + 0.5

class Costume(Textil):
    def __init__(self, height):
        self.height = height
    @property
    def get_square_costume(self):
        return self.height * 2 + 0.3

coat = Coat(44)
costume = Costume(190)

print('Площадь ткани на пальто - ', coat.get_square_coat)
print('Площадь ткани на костюм - ', costume.get_square_costume)
print('Итого нужно ткани - ', coat.get_square_coat + costume.get_square_costume)