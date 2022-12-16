# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

while 1:
    day = int(input ('Please enter digit: '))
    if day > 0 and day < 8:
        if day > 5:
            print('This day is weekend!')
        else:
            print('This day is NOT weekend!')
        break
    else:
        print ('Incorrect data, please repeat\n')




