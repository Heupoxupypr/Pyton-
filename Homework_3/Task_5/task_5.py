# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibo (k, dig_1, dig_2, p_fibo):
    if k:
        p_fibo.append(dig_2)
        fibo (k-1, dig_2, dig_1+dig_2, p_fibo)

def nega_fibo (k, dig_1, dig_2, n_fibo):
    if k:
        nega_fibo (k-1, dig_2, dig_1 - dig_2, n_fibo)
    n_fibo.append(dig_1)
   

# Попросим пользователя ввести число
number = int(input("Please enter number:\n"))
fibo_lst =list()

# Добавим в список отрицательные числа фибоначи
nega_fibo(number, 0, 1, fibo_lst)
# Добавим в список положительные числа фибоначи
fibo (number, 0, 1, fibo_lst)

# Выведем список на экран
print (fibo_lst)