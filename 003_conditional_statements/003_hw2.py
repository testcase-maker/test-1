import math

x = float(input('x= '))

if - math.pi <= x <= math.pi:
    y = math.cos(3 * x)
    print(y)
else:
    y = x
    print(y)
