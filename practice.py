quest = input('Привет, давай знакомиться, как тебя зовут?) ')
print(quest, '- прекрасное имя, а меня Настя зовут')
quest_1 = input('А лет тебе сколько? ')
print('Класс, тебе %s, а мне 22' % quest_1)
quest_2 = input('Хочешь фокус? ')
quest_3 = int(input('Это риторический вопрос, фокус будет в любом случае. Введи любое число: '))
import datetime
a = datetime.timedelta(seconds=quest_3)
print('Тадаааам, я сделала второе задание и перевела твоё число в часы и минуты, получилось', a)
quest_4 = input('Смотри ещё фокус! Введи другое число: ')
a = quest_4 + quest_4
b = quest_4 + a
answ_1 = int(quest_4) + int(a) + int(b)
print('Я сложила твоё число в формате n+nn+nnn и у меня получилось', answ_1)
quest_5 = abs(int(input('Давай теперь любое положительное число:')))
max_num = quest_5 % 10
while quest_5 >= 1:
    quest_5 = quest_5 // 10
    if quest_5 % 10 >= max_num:
        max_num = quest_5 % 10
    if quest_5 > 9:
        continue
    else:
        print('Максимальная цифра в числе -', max_num)
        break
money_1 = int(input('Давай теперь задачка с деньгами. Введи какую-нибудь цифру выручки: '))
money_2 = int(input('Теперь введи какую-нибудь цифру издержек: '))
if money_2 > money_1:
    print('Очень жаль, но компания работает в убыток')
else:
    print('Компания работает в прибыль с рентабельностью -', (money_1 - money_2) / money_1 * 100)
    peop = int(input('А сколько людей работает в компании? '))
    print('Прибыль фирмы на одного сотрудника =', money_1 / peop)
sport_a = int(input('Поехали дальше. Немного странный вопрос: Сколько км пробежал в первый день? '))
sport_b = int(input('А сколько надо? '))
day = 1
km = sport_a
while sport_b > km:
    km = km * 1.1
    day = day + 1
print('Победный день -', day)


