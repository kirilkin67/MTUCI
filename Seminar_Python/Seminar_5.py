from math import log, factorial


def square(number, view=''):
    result = number * number
    if view == 'print':
        print("Квадрат числа равен:", result)
    return result


def nums(num: int):
    res = [num - 1, num + 1]
    return res


def str_lower(my_str):
    return my_str.lower().split()


def my_log(numbers):
    res = []
    for number in numbers:
        try:
            res.append(log(number))
        except ValueError:
            res.append('None')
    return res


def create_dict_from_lists(array_1: list, array_2: list):
    res = {}
    if len(array_1) == len(array_2):
        for name in array_1:
            res[name] = array_2[array_1.index(name)]
    else:
        print('Списки имеют разную длину')
    return res


def binom_prob(p, n, k):
    return (factorial(n) // (factorial(k) * factorial(n - k))) * (p ** k) * ((1 - p) ** (n - k))


def all_sort(*args):
    return sorted(list(args))


if __name__ == '__main__':
    print(square(4))
    square(5, "print")
    print("-" * 80)
    print(nums(7))
    print("-" * 80)
    print(str_lower("В лесу родилась ёлочка В лесу она росла"))
    print("-" * 80)
    print(my_log([1, 3, 2.5, -1, 9, 0, 2.71]))
    print("-" * 80)
    print(create_dict_from_lists(["Ann", "Tim", "Sam"], [12, 23, 17]))
    print(create_dict_from_lists(["Ann", "Tim", "Sam"], [12, 23, 17, 45]))
    print("-" * 80)
    print(binom_prob(0.2, 50, 10))
    print("-" * 80)
    print(all_sort(7, 6, 1, 3, 8, 0, -2))
