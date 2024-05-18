from math import log


def ex1():
    fio = input('Введите свои фамилию, имя и отчество в строчку через пробел: ').title().split()
    print('Ваша фамилия: ', fio[0])
    print('Ваше имя: ', fio[1])
    print('Ваше отчество: ', fio[2])


def ex2():
    test_string = "1; 2; 3; 100"
    print(*[int(i) for i in (test_string.replace(' ', '').split(sep=';'))], sep=', ')
    print(*[float(i) for i in (test_string.replace(' ', '').split(sep=';'))], sep=', ')


def ex3():
    print(input('Введите номер телефона в формате 8-123-456-78-90 : ').replace('-', ''))


def ex4(array):
    return [round(log(element), 2) for element in array]


def ex5(words):
    words = [word.lower().replace(' ', '') for word in words]
    print(words)
    return words


if __name__ == '__main__':
    ex1()
    print("-" * 80)
    ex2()
    print("-" * 80)
    ex3()
    print("-" * 80)
    profit = ex4([10, 20, 30, 5, 15, 6])
    print(profit)
    print("-" * 80)
    my_words = ["Speak ", "to", "me ", "of", "Florence", "And ", "of", "the", "Renaissance"]
    ex5(my_words)
