print("Алгоритм поиска простых чисел!")
n = int(input("Введите конечное число "))
simple_number = []


for number in range(2, n+1):
    for check_num in range(2, number):
        if number % check_num == 0:
            break
    else:
        simple_number.append(number)

print(simple_number)
def mult():
    multip = 1
    for results in simple_number:
        multip *= results
    return multip


way = input("""Если вам нужне сумма данных чисел, 
введите 'sum' и нажмите  'Enter',
если вам нужно произведение введите 'mult' и нажмите 'Enter'
для выхода нажмите любую клавишу """)
if way == "sum":
    print('Сумма данных чисел ', sum(simple_number))
elif way == "mult":
    print('Произведение данных чисел ', mult())
else:
    exit(0)
