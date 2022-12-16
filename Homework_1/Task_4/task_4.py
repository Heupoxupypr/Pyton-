# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

while 1:
    quater = int(input ('Please enter number of quater: '))
    if quater > 0 and quater < 5:
        break
    else:
        print ('Incorrect quater\'s number, please repeat\n')

if quater == 1:
    print ('Range of values for X: 1 to Positive Infinity')
    print ('Range of values for Y: 1 to Positive Infinity')
elif quater == 2:
    print ('Range of values for X: -1 to Negative Infinity')
    print ('Range of values for Y: 0 to Positive Infinity')
elif quater == 3:
    print ('Range of values for X: -1 to Negative Infinity')
    print ('Range of values for Y: -1 to Negative Infinity')
elif quater == 4:
    print ('Range of values for X: 1 to Positive Infinity')
    print ('Range of values for Y: -1 to Negative Infinity')