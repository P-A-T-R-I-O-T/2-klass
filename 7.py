# Найти произведение цифр числа.
numbers = int (input("Введите цифры: "))
counter = 1
while numbers > 0:
    counter *= numbers %10
    numbers //= 10 
print(counter)