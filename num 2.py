my_list = []
num_1 = int(input('Сколько элементов будет в списке? '))
i = 0
el = 0
while i < num_1:
    my_list.append(input('Введите любое значение '))
    i+=1
print(my_list)
a = int(len(my_list))
if a % 2 == 0:
    for el in range(0, a, 2):
        my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
        el += 2
else:
    for el in range(0, a-1, 2):
        my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
        el += 2
print(my_list)