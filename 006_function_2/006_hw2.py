phrase = input("Давайте проверим или ваша фраза является палиндромом:")
phrase_list = list(phrase)
phrase_new = []


def make_list():
    global phrase_new
    for elements in phrase_list:
        if elements == ' ':
            pass
        else:
            phrase_new.append(elements)


def main():
    make_list()
    phrase_new_rev = list(reversed(phrase_new))
    if phrase_new_rev == phrase_new:
        print("Эта фраза является палиндромом!")
    else:
        print('Эта фраза не является палиндромом.')


print(phrase)
make_list()
main()
