# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# (если получаются длинные числа после запятой, это нормально и особенность данного языка программирования. 
# ваш ответ может не совпадать с примером(может получитя 0,20))
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# подключим random

import random as rnd

#Введем длину списка
n = int(input("Please enter list lenght:\n"))

# Заполним список случайными числами от 1 до 10

numbers = list()
for index in range(n):
    numbers.append(rnd.randint(1,10) + rnd.randint(1,99)/100)

# Выведем список на экран
print (f"Generate random list:\n{numbers}")

# Переменные для максимального и минимального значений дробной части

max = 0
min = 1

for index in range(n):
    if (round(numbers[index]%1,2)) > max:
        max = round(numbers[index]%1,2)
    if (round(numbers[index]%1,2)) < min:
        min = round(numbers[index]%1,2)    

print (f"Result: {max} - {min} = {max - min}")