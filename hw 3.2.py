fields = ['имя', 'фамилия', 'год рождения', 'город проживания', 'email', 'телефон']

data = {}
for field in fields:
    data[field] = input(f'Введите значение поля {field} - ')

print(data)
