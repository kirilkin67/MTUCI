from random import randint


def ex1():
    print('Молодец!') if int(input('Введите положительное число: ')) > 0 else print('Это не положительное число!')


def ex2(students):
    grades = {2: 'Плохо', 3: 'Удовлетворительно', 4: 'Хорошо', 5: 'Отлично'}
    for student in students:
        grade = randint(2, 5)
        print(f'{student} - "{grade}\n\t{grades[grade]}"')


def ex3():
    password = 'qwerty'
    if input('Password: ') == password:
        print('Login success')
    else:
        print('Incorrect password, try again!')
        ex3()


def ex4():
    favorites = [3, 7, 11, 23, 18, 48, 81]
    print("Мое любимое число!") if int(input('Введите целое число: ')) in favorites else print("Эх, ну почему?")


def ex5():
    print("Это число нечётное") if int(input('Введите целое число: ')) % 2 else print("Это число чётное")


def ex6():
    print("Это имя собственное") if input('Введите имя: ').istitle() else print("Это имя нарицательное")


if __name__ == '__main__':
    ex1()
    print("-" * 80)
    studs_list = ['Иван', 'Петр', 'Мария', 'Елена', 'Михаил']
    ex2(studs_list)
    print("-" * 80)
    ex3()
    print("-" * 80)
    ex4()
    print("-" * 80)
    ex5()
    print("-" * 80)
    ex6()
