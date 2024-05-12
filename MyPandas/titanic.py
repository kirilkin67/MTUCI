import pandas as pd
from matplotlib import pyplot as plt
from pandas import DataFrame

TITANIC_FILE_PATH = "Resources/TitanicBase.csv"


def draw_histogram(data_frame: DataFrame, col_name):
    histogram = data_frame[col_name].plot.hist(color='red')
    histogram.set_title(f'Название колонки - {col_name}')
    histogram.set_xlabel(col_name)
    histogram.set_ylabel("Количество пассажиров")
    plt.show()


def rename_column(df_columns: list, index: int, new_name: str):
    df_columns[index] = new_name
    return df_columns


def line_break(ex_name: str):
    print(f'\n{ex_name}')
    print("-" * 80)


def add_column_female(column: str):
    return column.replace("female", "1").replace("male", "0")


if __name__ == '__main__':
    line_break('ex_1')
    titanic_base = pd.read_csv(TITANIC_FILE_PATH)
    print(titanic_base.info())
    print(titanic_base.head(2))

    line_break('ex_2')
    titanic = pd.read_csv(TITANIC_FILE_PATH, index_col='PassengerId')
    print(titanic.info())
    print(titanic.head(2))
    print("Сводная статистическая информация по БД", titanic.describe(), sep='\n')

    line_break('ex_3')
    titanic.dropna().to_csv("Resources/Titanic.csv")
    titanic.dropna().to_excel("Resources/TitanicExel.xlsx", sheet_name="passengers", index=False)

    line_break('ex_4')
    titanic = pd.read_csv("Resources/Titanic.csv", index_col='PassengerId')
    print(titanic.info())

    line_break('ex_5')
    print("Сводная статистическая информация по БД", titanic.describe(), sep='\n')

    draw_histogram(titanic, "Age")

    line_break('ex_7')
    describe_col = titanic['Fare'].describe()
    print(f'Статистики для столбца "Стоимость билета (Fare)"', describe_col, sep='\n')

    line_break('ex_8')
    columns = list(titanic.columns)
    print(f"Названия столбцов в базе данных", columns, sep='\n')

    line_break('ex_9')
    """ Переименуйте столбец с классом пассажира из Pclass в Class. """
    titanic.columns = rename_column(columns, 1, "Class")
    print(list(titanic.columns))

    line_break('ex_10')
    """ Выберите из базы данных все строки, которые соответствуют пассажирам женского пола,
    и сохраните их в новую базу female. """
    titanic = pd.read_csv(TITANIC_FILE_PATH, index_col='PassengerId')
    titanic = titanic.rename(columns={"Pclass": "Class"})
    print(list(titanic.columns))
    titanic[(titanic["Sex"] == 'female')].to_csv("Resources/female.csv")
    female = pd.read_csv("Resources/female.csv")
    print(female.shape)

    line_break('ex_11')
    """ Выберите из базы данных все строки, которые соответствуют выжившим пассажирам мужского пола младше 32 лет,
    и сохраните их в базу Ymale. """
    y_male = titanic[(titanic["Survived"] == 1)
                     & (titanic["Sex"] == 'male')
                     & (titanic["Age"] < 32)]
    y_male.to_csv("Resources/YmaleSurvived.csv")
    y_male.to_excel("Resources/YmaleSurvived.xlsx", sheet_name="yang_male", index=False)
    print(y_male.shape)

    line_break('ex_12')
    """ Выберите из базы данных все строки, которые соответствуют пассажирам 1 или 2 класса. """
    class_1_2 = titanic[(titanic["Class"] == 1) | (titanic["Class"] == 2)]
    print(class_1_2.shape)

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
    # titanic["Female"] = add_column_female(titanic["Sex"].str)
    # titanic.insert(11, "Female", add_column_female(titanic["Sex"].str))
    print(titanic.info())
    print(titanic.head())
    titanic.to_excel("Resources/TitanicExel.xlsx", sheet_name="passengers", index=False)

    line_break('ex15')
    """ Выведите на экран все уникальные значения в столбце Embarked """
    embarked = titanic["Embarked"].dropna()
    print(embarked.unique())

    line_break('ex16')
    quantitative = titanic[["Survived", "Class", "Age", "Fare"]]
    """ Сгруппируйте строки в датафрейме в соответствии со значениями переменной Survived и выведите средние значения 
    всех количественных переменных по группам."""
    print(quantitative.groupby("Survived").agg('mean'))

    line_break('ex17')
    """Сгруппируйте строки в датафрейме в соответствии со значениями переменной Sex и сохраните в отдельный датафрейм 
    таблицу со средними и медианными значениями переменной Age по группам(мужчины и женщины)."""
    quantitative = titanic[["Sex", "Age"]].dropna()
    group_by_sex = quantitative.groupby("Sex").agg(['mean', 'median'])
    print(group_by_sex)

    line_break('ex_18')
    """ Приведите все названия столбцов в датафрейме к нижнему регистру и сохраните изменения """
    titanic = titanic.rename(columns=str.lower)
    print(list(titanic.columns))

    line_break('ex_19')
    """ Выгрузите итоговый датафрейм в файл Titanic-new.csv """
    titanic.to_csv("Resources/Titanic-new.csv")
    titanic.to_excel("Resources/Titanic-new.xlsx", sheet_name="passengers", index=False)
