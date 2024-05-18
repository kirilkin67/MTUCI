def ex1(numbers: list, variant: int):
    return list(map(lambda x: x * (variant + 7), numbers))


def ex2(num1, num2):
    return list(map(lambda x, y: x * y, num1, num2))


def ex3(numbers, variant):
    sub_result = list(map(lambda x: x * variant, numbers))
    result_odd = list(filter(lambda x: x % 2, sub_result))
    result_even = list(filter(lambda x: not (x % 2), sub_result))
    return result_odd, result_even


def ex4(numbers):
    div_int = list(map(lambda x: int(x) // my_variant, numbers))
    div_float = list(map(lambda x: round(float(x) / my_variant, 2), numbers))
    return div_int, div_float


if __name__ == '__main__':
    my_variant = 5
    list_one = [12, 24, 36, 48, 109, 187]
    print(ex1(list_one, my_variant))
    print("-" * 80)

    number_one = [7, 9, 2, 6, 1, 2, 3, 4, 5, 6, 7]
    number_two = [7, 9, 2, 6, 9, 8, 7, 6, 5, 4, 3]
    print(ex2(number_one, number_two))
    print("-" * 80)

    print(*ex3(number_one, my_variant), sep='\n')
    print("-" * 80)

    number_str = ['7', '9', '2', '6', '1', '2', '3', '4', '5', '6', '7']
    print(*ex4(number_str), sep='\n')
