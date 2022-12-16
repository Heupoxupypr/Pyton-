# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка .
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

while 1:
    x = int(input ('Please enter X: '))
    if x:
        break
    else:
        print ('Incorrect X, please repeat\n')

while 1:
    y = int(input ('Please enter Y: '))
    if y:
        break
    else:
        print ('Incorrect Y, please repeat\n')

print(f'Point coordinate: [{x};{y}]')

if x > 0 and y > 0:
    print('Quater 1')
elif x < 0 and y > 0:
    print('Quater 2')
elif x < 0 and y < 0:
    print('Quater 3')
elif x > 0 and y < 0:
    print('Quater 4')
