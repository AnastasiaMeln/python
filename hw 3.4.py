x = float(input('Введите положительное число x: '))
y = int(input('Введите целое отрицательное число: '))
def my_func (x, y):
    if x <=0 or y >= 0:
        print('Ошибка! Числа не соответствуют условиям')
    else:
        return 1 / x ** abs(y)

print(my_func(x, y))

