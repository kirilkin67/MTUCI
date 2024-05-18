from math import log


def ex0():
    a = [1, 0, 9, 12, 18, 34, 89, 91, 33, 127]
    b = [2, 8, 9, 11, 76, 25, 44]
    print(a[0], a[2], a[-1])
    b.append(7)
    a[4] = 8
    merged = a[:] + b[:]
    print(merged)
    c = a[:]
    c[-1] = 100
    print(c)


def ex1():
    girls = ["Иветта", "Виолетта", "Кассандра", "Вирджиния", "Амелия", "Розамунда", "Янина"]
    print(girls[1: 5])
    new_girls = girls[:]
    new_girls.append('Беатриса')
    print(new_girls[3:])
    print(girls[:4])
    print([girls[2], girls[4], girls[5]])


def ex2():
    L = [12, 3, 8, 125, 10, 98, 54, 199]
    print(*L, sep=', ')
    print(*(list(map(lambda x: log(x), L))), sep=', ')
    L[4] = 0
    l_log_new = []
    for element in L:
        try:
            l_log_new.append(log(element))
        except ValueError:
            l_log_new.append('некорректное значение')
    print(*l_log_new, sep=', ')


def ex3():
    age = [24, 35, 42, 27, 45, 48, 33]
    age2 = [value * value for value in age]
    print(age2)


def ex4():
    numbers = [1, 5, 6, 8, 10, 21, 25, 1, 0, -9, 9]
    user_in = int(input('Введите целое число от 1 до 10: '))
    if user_in in range(1, 11):
        print(numbers[int(user_in) - 1])
    return


def ex5():
    array = [1, 2, 3, 4]
    for i in range(len(array)):  # последовательно для всех элементов списка
        summa = array[i] + array[i - 1]  # текущий + предыдущий элемент списка ('-1' - последний эл-т)
        print(summa)


if __name__ == '__main__':
    ex0()
    print("-" * 80)
    ex1()
    print("-" * 80)
    ex2()
    print("-" * 80)
    ex3()
    print("-" * 80)
    ex4()
    print("-" * 80)
    ex5()
