# Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
string = input ('введите 10 цифр: ')
if not string.isdigit():
    print ('Вы ввели не цыфры!')
    string = input ('введите 10 цифр: ')
elif len (string) < 10:
    print ('Вы ввели слишком мало цифр!')
    string = input ('введите 10 цыфр: ')
elif len (string) > 10:
    print ('Вы ввели слишком много цифр!')
    string = input ('введите 10 цыфр: ')
else:   
    counting = 0
    for meaning in string:
        if meaning == '5':
            counting = counting + 1
    print (str(counting))
