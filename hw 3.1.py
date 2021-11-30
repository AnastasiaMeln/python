a = int(input('Введите числитель: '))
b = int(input('Введите знаменатель: '))
def my_math(a, b):
    return a / b
if b == 0:
    b = int(input('Делят на ноль только лузеры, подумай ещё раз: '))
    if b == 0:
        print('Ты безнадёжен')
    else:
        print(my_math(a, b))
else:
    print(my_math(a, b))
