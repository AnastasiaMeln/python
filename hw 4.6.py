from itertools import count, cycle

for el in count (1):
    if el > 20:
        break
    else:
        print(el)

i = 1
for el in cycle("MyNameIsNastya"):
    if i > 14:
        break
    else:
        print(el)
        i += 1