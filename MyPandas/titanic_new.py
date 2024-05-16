import pandas as pd
from matplotlib import pyplot as plt
from pandas import DataFrame


def draw_histogram(data_frame: DataFrame, col_name):
    histogram = data_frame[col_name].plot.hist(color='red')
    histogram.set_title(f'Название колонки - {col_name}')
    histogram.set_xlabel(col_name)
    histogram.set_ylabel("Количество пассажиров")
    plt.show()


def line_break(ex_name: str):
    print(f'\n{ex_name}')
    print("-" * 80)


if __name__ == '__main__':
    line_break('ex_1')
    titanic_base = pd.read_csv("Titanic.csv")
    print(titanic_base.info())
    print(titanic_base.head(2))

    line_break('ex_2')
    titanic = pd.read_csv("Titanic.csv", index_col='PassengerId')
    print(titanic.info())
    print(titanic.head(2))
    print("Сводная статистическая информация по БД", titanic.describe(), sep='\n')

    line_break('ex_3')
    titanic_not_empty = titanic.dropna()
    print(titanic_not_empty.info())
    titanic_not_empty.to_csv("TitanicNotEmpty.csv")

    line_break('ex_4')
    titanic = pd.read_csv("Titanic.csv", index_col='PassengerId')
    print(titanic.info())

    line_break('ex_5')
    print("Сводная статистическая информация по БД", titanic.describe(), sep='\n')

    draw_histogram(titanic, "Age")

    line_break('ex_7')
    """ Выведите описательные статистики для столбца Стоимость билета (Fare) """
    describe_fare = titanic['Fare'].describe()
    print(f'Статистики для столбца "Стоимость билета (Fare)"', describe_fare, sep='\n')

    line_break('ex_8')
    """ Выведите названия столбцов в базе данных в виде списка (объект типа list) """
    columns = list(titanic.columns)
    print(f"Названия столбцов в базе данных", columns, sep='\n')

    line_break('ex_9')
    """ Переименуйте столбец с классом пассажира из Pclass в Class. """
    titanic = titanic.rename(columns={"Pclass": "Class"})
    print(f"Названия столбцов в базе данных", list(titanic.columns), sep='\n')

    line_break('ex_10')
    """ Выберите из базы данных все строки, которые соответствуют пассажирам женского пола,
    и сохраните их в новую базу female. """
    titanic = pd.read_csv("Titanic.csv", index_col='PassengerId')
    titanic = titanic.rename(columns={"Pclass": "Class"})

    female = titanic[(titanic["Sex"] == 'female')]
    female.to_csv("female.csv")
    print(female.shape)
    print(female.head(4))

    line_break('ex_11')
    """ Выберите из базы данных все строки, которые соответствуют выжившим пассажирам мужского пола младше 32 лет,
    и сохраните их в базу Ymale. """
    y_male = titanic[(titanic["Survived"] == 1)
                     & (titanic["Sex"] == 'male')
                     & (titanic["Age"] < 32)]
    y_male.to_csv("YmaleSurvived.csv")
    print(y_male.shape)
    print(y_male.head(3))

    line_break('ex_12')
    """ Выберите из базы данных все строки, которые соответствуют пассажирам 1 или 2 класса. """
    class_1_2 = titanic[(titanic["Class"] == 1) | (titanic["Class"] == 2)]
    print(class_1_2.shape)
    print(class_1_2.head(3))

    line_break('ex_13')
    """ Выберите из базы данных все строки, которые соответствуют выжившим пассажирам 1 или 2 класса. """
    class_1_2 = class_1_2[class_1_2["Survived"] == 1]
    print(class_1_2.shape)
    survived_class_1_2 = titanic[((titanic["Class"] == 1) | (titanic["Class"] == 2)) & (titanic["Survived"] == 1)]
    print(survived_class_1_2.shape)
    print(class_1_2.head(2))

    line_break('ex_14')
    """
    Добавьте в дата фрейм столбец Female, состоящий из значений 0 и 1, где 1 соответствует пассажирам женского пола
    """
    titanic["Female"] = titanic["Sex"].replace({"female": "1", "male": "0"})
    print(titanic.info())
    print(titanic.head())
    titanic.to_excel("TitanicExel.xlsx", sheet_name="passengers", index=False)

    line_break('ex15')
    """ Выведите на экран все уникальные значения в столбце Embarked """
    embarked = titanic["Embarked"].dropna()
    print(embarked.unique())

    line_break('ex16')
    quantitative = titanic[["Survived", "Class", "Age", "Fare"]]
    """ Сгруппируйте строки в дата фрейме в соответствии со значениями переменной Survived и выведите средние значения 
    всех количественных переменных по группам."""
    print(quantitative.groupby("Survived").agg('mean'))

    line_break('ex17')
    """Сгруппируйте строки в дата фрейме в соответствии со значениями переменной Sex и сохраните в отдельный датафрейм 
    таблицу со средними и медианными значениями переменной Age по группам(мужчины и женщины)."""
    quantitative = titanic[["Sex", "Age"]].dropna()
    group_by_sex = quantitative.groupby("Sex").agg(['mean', 'median'])
    print(group_by_sex)

    line_break('ex_18')
    """ Приведите все названия столбцов в дата фрейме к нижнему регистру и сохраните изменения """
    titanic = titanic.rename(columns=str.lower)
    print(list(titanic.columns))

    line_break('ex_19')
    """ Выгрузите итоговый датафрейм в файл Titanic-new.csv """
    titanic.to_csv("Titanic-new.csv")
