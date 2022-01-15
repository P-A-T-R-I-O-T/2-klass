# Вывести цифры числа на каждой строчке.
# Вывести цифры числа на каждой строчке, с лево на право.
integer_number = 2129
while integer_number>0:
    integer_number //= 10
    a = integer_number %10
    if integer_number %10 == 0:
       print (9)
    else:
        n = a
        print(n)

# Вот этот код работает не коректно. Выводит: 9 212
#print(integer_number%10,integer_number//10)


#Вот этот код работает с права на лево. Не интересно...

#while integer_number>0:
#    print(integer_number%10)
#    integer_number = integer_number//10
