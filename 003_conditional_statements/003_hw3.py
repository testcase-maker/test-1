print('I can solve quadratic equation "ax^2 + bx + c = 0"')

a = float(input('a= '))
b = float(input('b= '))
c = float(input('c= '))

d = b ** 2 - 4 * a * c

x1 = (- b + ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a)
x2 = (- b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
x3 = - (b / (2 * a))
x11 = round(x1, 2)
x12 = round(x2, 2)
x13 = round(x3, 2)

if d < 0:
    print("No solutions")
elif d == 0:
    print("Only one solution {}".format(x13))
else:
    print(f"We have two solutions {x11} and {x12}")
