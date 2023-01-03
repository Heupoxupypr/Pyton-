# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# подключим random

import random as rnd

#Введем длину списка
n = int(input("Please enter list lenght:\n"))

# Заполним список случайными числами от 1 до 100

numbers = list()
for index in range(n):
    numbers.append(rnd.randint(1,100))

# Выведем список на экран
print (f"Generate random list:\n{numbers}")

# Переменная для суммы элементов на нечетных позициях в списке
sum = 0

for index in range(n):
    if index%2:
        print (f"{index}:{numbers[index]}")
        sum+=numbers[index]

print(f"Summ of elements: {sum}") 