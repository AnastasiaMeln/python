my_list = [7, 5, 5, 3, 1]
new_1 = int(input('Введите новый элемент рейтинга: '))
i = 0
for n in my_list:
    if new_1 <= n:
        i += 1
my_list.insert(i, new_1)
print(my_list)