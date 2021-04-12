print("Я могу нарисовать прямоугольник")

i = int(input('Введите высоту '))
j = int(input('Введите ширину '))

for t in range(i):
    print('*' * j, end='')
    print()
