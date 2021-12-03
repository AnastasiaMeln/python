from sys import argv
time, money, more_money = map(float, argv[1:])
ZP = (time * money) + more_money
print(f'Зарплата - {ZP}')