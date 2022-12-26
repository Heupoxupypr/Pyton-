# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

# Запрашиваем у пользователя число N
n = int(input("Please enter number: "))
sum = 0

# Создаем пустой список
x_lst = list()

#Заполняем список согласно формуле (1+1/n)**n и сразу ссумируем полученные элементы
for i in range(1,n+1):
    x_lst.append((1+1/i)**i)
    sum += x_lst[i-1]

print (x_lst)
print (f"Summ all numbers in list: {sum}")