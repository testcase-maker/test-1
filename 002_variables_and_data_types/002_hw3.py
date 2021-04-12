print('I can risolve quadratic equation "ax^2 + bx + c = 0"')

a = float(input('Give me a:'))
b = float(input('Give me b:'))
c = float(input('Give me c:'))

d = b ** 2 - 4 * a * c
x1 = (- b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
x2 = (- b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
x11 = round(x1, 2)
x12 = round(x2, 2)

if d < 0:
    print("No solutions")
elif d == 0:
    print("Only one solution {}".format(x11))
else:
    print(f"We have two solutions {x11} and {x12}")
