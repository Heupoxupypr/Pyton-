# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int (input("Please enter digit: "))

mult = 1
# определяем цикл с диапазоном значений от 1 до N
for i in range (1,N+1):
    # print (i)
    mult *= i

print (f"Multiplication all numbers from 1 to {N}: {mult}")