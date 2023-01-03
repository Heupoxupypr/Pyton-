# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# подключим random

import random as rnd

#Введем длину списка
n = int(input("Please enter list lenght:\n"))

# Заполним список случайными числами от 1 до 10

numbers = list()
for index in range(n):
    numbers.append(rnd.randint(1,10))

# Выведем список на экран
print (f"Generate random list:\n{numbers}")

mult_lst = list()

for index in range (int(n/2)):
    mult_lst.append(numbers[index] * numbers[-1 - index])

# Выведем полученный список
print(f"Result list: {mult_lst}")