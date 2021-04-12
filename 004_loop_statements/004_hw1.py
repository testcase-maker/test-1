print("Сумма чисел от а до b при условии что 'a<b'")

a = int(input("Введите значение 'a'"))
b = int(input("Введите значение 'b'"))
x = 0

if a < b:
    for c in range(a, b + 1):
        x += c
       # print(x)
else:
    print('a должно быть меньше b')
print(x)