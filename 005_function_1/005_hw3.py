print("Привет, я калькулятор!")

while True:
    way = input('''
    Если хотите выйти введите - exit
    Если хотите продолжить нажмите клавишу Enter ''')
    if way == 'exit':
        exit(0)
    exemple = input("Введите данные в таком виде: 'a + b' и нажмите Enter ")
    a = int(exemple[0])
    b = int(exemple[2])
    c = exemple[1]



    def plus():
        x = a + b
        print("Ответ:", x)


    def min():
        x = a - b
        print("Ответ:", x)


    def mult():
        x = a * b
        print("Ответ:", x)


    def div():
        if b == 0:
            print("На ноль делить нельзя")
        else:
            x = a / b
            print("Ответ:", x)


    if __name__ == '__main__':
        def solve():
            if c == "+":
                plus()
            elif c == "-":
                min()
            elif c == "*":
                mult()
            elif c == "/":
                div()

    solve()