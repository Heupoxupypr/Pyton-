# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат. 

x = list()

for i in range(3):
    x.append(int(input(f"Please enter digit {i+1}: ")))

print(x)

if (not(x[0] or x[1] or x[2])) == ((not x[0]) and (not x[1]) and (not x[2])):
    print('Mathematical expression ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
    print(True)
else:
    print(False)