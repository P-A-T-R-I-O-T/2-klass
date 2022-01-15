# Найти максимальную цифру в числе
num =int(input("Введите цифры: "))
maximum = num % 10
num = num // 10
while num > 0:
    if num % 10 > maximum:
        maximum = num % 10
    num = num // 10
print(maximum)