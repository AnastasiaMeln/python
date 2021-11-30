arg1 = int(input('Введите первый аргумент: '))
arg2 = int(input('Введите второй аргумент: '))
arg3 = int(input('Введите третий аргумент: '))
def my_finc (arg1, arg2, arg3):
    my_list = [arg1, arg2, arg3]
    a = min(my_list)
    my_list.remove(a)
    return sum(my_list)
print(my_finc(arg1, arg2, arg3))