# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в отдельном списке
# ( пример n=4, lst1=[4,-2,1,3] - списко на основе n, а позиции элементов lst2=[3,1].

import random as rnd

# Запрашиваем у пользователя число N
N = int(input("Please enter number: "))

# создадим список из N элементов и заполним его рандомными значениями промежутка [-N,N]
N_lst = list()

for index in range (N):
    N_lst.append(rnd.randint(-N,N))

print (f"Generate random list:\n{N_lst}")

#Создадим список произвольного размера от 1 до N и заполним его рандомными номерами позиций из 1-го списка
Pos_lst = list()

for index in range(rnd.randint(1,N)):
    Pos_lst.append(rnd.randint(0,N-1))

print (f"Generate random positions list:\n{Pos_lst}")

# перемножим элементы из списка 1 на позициях из списка 2
mult = 1

for index in Pos_lst:
    print(f"{index}:{N_lst[index]} ", end=' ')
    mult *= N_lst[index]
print()
print(f"Multiplication elments: {mult}")