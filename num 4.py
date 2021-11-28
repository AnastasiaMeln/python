a = input('Введите несколько значений через пробел: ')
b = a.split()
print(b)
for i, el in enumerate(b, 1):
    print(i, el[:10])
