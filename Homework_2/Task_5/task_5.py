#Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)

import random as rnd

# Запрашиваем у пользователя длину списка
N = int(input("Please enter len of list: "))

# создадим список из N элементов и заполним его рандомными значениями промежутка [-N,N]
N_lst = list()

for index in range (N):
    N_lst.append(rnd.randint(-N,N))

print (f"Generate random list:\n{N_lst}")

# Алгоритм будет заключаться в том, что в цикле от 0 до N для каждого элемента списка будет генерироваться рандомно новая позиция
# и затем элементы будут меняться местами

new_ind = 0
last_el = 0

for index in range(N):
    new_ind = rnd.randint(0,N-1)
    last_el = N_lst[index]
    N_lst[index] = N_lst[new_ind]
    N_lst[new_ind] = last_el

print (f"Generated list after shake:\n{N_lst}")