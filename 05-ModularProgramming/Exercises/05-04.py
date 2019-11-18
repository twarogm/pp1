import math

x = 3.7
y = 4

sqrtX = math.sqrt(x)
XtopowY = math.pow(x, y)
YrootX = math.pow(x, (1/y))
circleY = 2*(math.pi)*y**2
factorialY = math.factorial(y)
floorX = math.floor(x)

print(f'x = {x}, y = {y}')
print(f'Pierwiastek kwadratowy x = {sqrtX}')
print(f'x do potęgi y = {XtopowY}')
print(f'Pierwiastek z x stopnia y = {YrootX}')
print(f'Pole koła o promieniu y = {circleY}')
print(f'Silnia z y = {factorialY}')
print(f'Największa liczba całkowita mniejsza lub równa od x = {floorX}')