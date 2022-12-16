# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print('Please enter coordinate of point А:')
ax=float(input('x='))
ay=float(input('y='))
 
print('Please enter coordinate of point B:')
bx=float(input('x='))
by=float(input('y='))
 
# по теореме Пифагора гипотенуза (расстояние) равно a^2 + b^2 = c^2
dist=((ax-bx)**2+(ay-by)**2)**0.5 # в степени 0.5 значит квадратный корень
 
print(f'Distance from point A to point B {dist:.2f}')