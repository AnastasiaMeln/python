stix = open("Borodino.txt", "r", encoding="utf-8")
content = stix.readlines()
print(len(content))
line_n = 0
words_n = 0
for el in content:
    line_n += 1
    words = el.split()
    print(words)
    words_n = len(words)
    print(words_n)