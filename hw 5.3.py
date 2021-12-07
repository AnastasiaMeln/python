with open ('money.txt', 'r', encoding='utf-8') as f:
    people = {line.split()[0]: int(line.split()[1]) for line in f}
    print(people)
    print('Средняя зп - ', sum(people.values()) / len(people))
    for i in people.items():
        if i[1] < 20000:
            print('В списке самых бедных в компании - ', i[0])
