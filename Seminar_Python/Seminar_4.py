def ex1(rept):
    rept["snake"] = "змея"
    rept["tortoise"] = "черепаха"
    rept["tortoise"] = rept.pop("tortoize")
    for animals in rept:
        print(rept[animals].title(), 'по-английски будет', animals)


def ex2():
    cnt = ["Andorra", "Belarus", "Denmark", "Kenya", "Jamaica", "Romania"]
    fh = [1.0, 6.0, 1.0, 4.0, 2.5, 2.0]
    freedom_dict = {}
    for country in cnt:
        freedom_dict[country] = fh[cnt.index(country)]
    print(freedom_dict)


def ex3():
    pairs = [(2, 4), (4, 6), (0, 1), (5, 2), (9, 1), (3, 8)]
    calc = {}
    for pair in pairs:
        calc[pair] = pair[0] * pair[1]
    print(calc)


def ex4(grades):
    excel, good, satisf, bad = [], [], [], []
    for stud in grades:
        if grades[stud] == 5:
            excel.append(stud)
        elif grades[stud] == 4:
            good.append(stud)
        elif grades[stud] == 3:
            satisf.append(stud)
        else:
            bad.append(stud)
    print('excel: ', excel)
    print('good: ', good)
    print('satisf: ', satisf)
    print('bad: ', bad)


if __name__ == '__main__':
    rept = {"python": "питон", "anaconda": "анаконда", "tortoize": "черепаха"}
    ex1(rept)
    print("-" * 80)
    ex2()
    print("-" * 80)
    ex3()
    print("-" * 80)
    grades = {'Anna': 4, 'Bob': 3, 'Claire': 5, 'Dick': 2, 'Elena': 5, 'Fred': 5, 'George': 4, 'Kristina': 3, 'Nick': 2,
              'Ursula': 4, 'Viktor': 5}
    ex4(grades)
