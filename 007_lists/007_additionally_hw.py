def main():
    list_of_strings = ["Список - изменяемый тип данных", "Строка - неизменяемый тип данных",
                       "Для обхода последовательности используйте совместный цикл",
                       "Строковый метод работает быстрее, чем срез"]
    print(list_of_strings)
    print('В данном списке, можно найти слова начинающиеся на определённую букву!')

    letter = input('Введите букву ')

    print(list_c(list_of_strings, letter))


def list_c(list_of_strings, letter):
    list_with_c = []
    list_of_strings_new = []
    final_list = []
    for sentence in list_of_strings:
        list_of_strings_new.append(sentence.lower().split())
    for element in list_of_strings_new:
        list_with_c.extend(element)
    for word in list_with_c:
        if word.startswith(letter):
            final_list.append(word)
    print(final_list)


if __name__ == '__main__':
    main()
