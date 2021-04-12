print('Сколькими способами можно подняться\n'
      'на заданную ступеньку, \n'
      'ступив на ступеньку вперёд\n'
      'или через одну?')
n = int(input('Введите количество ступенек: '))
m = n + 1

def scale(m):
    if m == 1 or m == 2:
        return 1
    else:
        return scale(m - 1) + scale(m - 2)


print(scale(m))
