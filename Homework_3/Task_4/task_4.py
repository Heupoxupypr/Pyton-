# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# Попросим пользователч ввести десятичное число
number = int(input("Please enter number:\n"))

# Создадим список для разрядов двоичного числа

bin_dif = list()

# Преобразуем десятичное число в двоичное
while number > 1:
    bin_dif.append(number - 2*int(number/2))
    number = int(number/2)

if number == 1:
    bin_dif.append(number)

# print (bin_dif)
# Выведем полученное число
for index in range (len(bin_dif)-1,-1,-1):
    print (bin_dif[index], end='')