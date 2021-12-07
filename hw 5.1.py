my_f = open("text.txt", "w", encoding='utf-8')
while True:
    line = input('Введите данные - ')
    my_f.write(f'{line}\n')
    if not line:
        break
my_f.close()
