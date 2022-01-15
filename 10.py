# Найти количество цифр 5 в числе
string = int(input ('введите цифры: '))
compare = string % 10
counting = 0
while string > 0:
    if string % 10 == 5:
        counting = counting + 1
    string = string // 10
print(counting)