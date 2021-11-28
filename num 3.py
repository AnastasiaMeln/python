a = int(input('Введите номер месяца: '))
list_win = [1, 2, 12]
list_spr = [3, 4, 5]
list_sum = [6, 7, 8]
list_aut = [9, 10, 11]
if a in list_win:
    print('Время года - зима')
elif a in list_spr:
    print('Время года - весна')
elif a in list_sum:
    print('Время года - лето')
else:
    print('Время года - осень')
month = int(input('Введите номер месяца: '))
seasons_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
if month == 1 or month == 12 or month == 2:
    print(seasons_dict.get(1))
elif month == 3 or month == 4 or month == 5:
    print(seasons_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
else:
    print(seasons_dict.get(4))