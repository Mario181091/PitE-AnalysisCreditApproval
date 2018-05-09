import numpy as np

import pandas as pd
import matplotlib.pyplot as plt
import random

import seaborn

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data"
names = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16']
dataset = pd.read_csv(url, names=names)


def repair_missing_value_numerical_attribute(attribute):
    mean = np.mean(pd.to_numeric(dataset[attribute], errors='coerce')).round()
    dataset[attribute] = dataset[attribute].replace(['?'], str(mean))


# ***************************************************    AGE **********************************************************


def set_class_age():
    age = pd.to_numeric(dataset.A2).astype(int)
    dataset["class_Age"] = age


def log_trasformation_age():
    age = pd.to_numeric(dataset.class_Age).astype(int)
    dataset["class_log_Age"] = np.log(age)


def print_basic_histogram_age(data):
    plt.figure(figsize=(10, 6))
    plt.hist(data.dropna(), bins=30, facecolor='green', alpha=0.70)
    plt.ylabel('# count ')
    plt.xlabel('Age')
    plt.show()


def print_basic_histogram_log_age(data):
    plt.figure(figsize=(10, 6))
    plt.hist(data.dropna(), bins=30, facecolor='green', alpha=0.95)
    plt.ylabel('# count ')
    plt.xlabel('Age (logarithm)')
    plt.show()


# ***************************************************    SEX **********************************************************


def set_class_sex():
    dataset["A1"] = dataset["A1"].replace(['a'], 0)
    dataset["A1"] = dataset["A1"].replace(['b'], 1)
    dataset["A1"] = dataset["A1"].replace(['?'], random.randint(0, 1))


def print_basic_histogram_sex(data):
    plt.figure(figsize=(10, 6))
    plt.hist_params = {'normed': False, 'bins': 20, 'alpha': 0.3}
    plt.hist(data)
    plt.ylabel('# count ')
    plt.xlabel('class_Sex')
    plt.show()


# ***************************************************    YEARS OF WORK ************************************************


def set_class_years_of_work():
    years = pd.to_numeric(dataset.A8).astype(int)
    dataset["class_Years_of_works"] = years


def print_basic_histogram_years_of_work(data):
    plt.figure(figsize=(10, 6))
    plt.hist(data.dropna(), bins=30, facecolor='blue', alpha=0.75)
    plt.ylabel('# count ')
    plt.xlabel('Years_Of_Work')
    plt.show()


# ***************************************************    INCOME *******************************************************


def print_basic_histogram_income(data):
    plt.figure(figsize=(10, 6))
    plt.hist(data.dropna(), bins=30, facecolor='red', alpha=0.90)
    plt.ylabel('# count ')
    plt.xlabel('Income')
    plt.show()


def class_for_income(row):
    if row.A15 >= 20000:
        return "High Income"
    elif 10000 <= row.A15 < 20000:
        return "High-Medium Income"
    elif 500 <= row.A15 < 10000:
        return "Medium Income"
    elif 250 <= row.A15 < 500:
        return "Medium-Low Income"
    elif row.A15 < 250:
        return "Low Income"


# *************************************************** correlation APPROVAL ********************************************


def set_class_approval():
    dataset["A16"] = dataset["A16"].replace(['+'], 1)
    dataset["A16"] = dataset["A16"].replace(['-'], 0)


def print_sex_correlation():
    print("\n correlation between sex and credit card approval")
    print(dataset.groupby(['A1', 'A16'])[['A16']].count())
    return dataset.groupby(['A1', 'A16'])[['A16']].count()


def print_sex_positive_approval():
    print("% positive credit card approval based on sex")
    print(dataset.groupby('A1')[['A16']].aggregate(['mean', "count"]), "\n")


def print_income_correlation():
    print("\n % credit card approval based on Income range")
    print(dataset.groupby('class_Income')[['A16']].mean(), "\n")
    return dataset.groupby('class_Income')[['A16']].mean()


def print_years_of_work_correlation():
    print("\n % credit card approval based on years of work")
    print(dataset.groupby('class_Years_of_works')[['A16']].aggregate(['mean', "count"]), "\n")
    # return dataset.groupby('class_Income')[['A16']].mean()


def print_average_years_of_work_approval():
    print("average years of work based on credit card approval")
    print(dataset.groupby('A16')[['class_Years_of_works']].mean(), "\n")


def print_average_income_approval():
    print("average income based on credit card approval")
    print(dataset.groupby('A16')[['A15']].mean(), "\n")


def print_average_age_approval():
    print("average age based on credit card approval")
    print(dataset.groupby('A16')[['class_Age']].mean(), "\n")


def print_basic_pie_income_approval(res):
    plt.figure(figsize=(10, 6))
    values = [res.A16[0], res.A16[1], res.A16[2], res.A16[3], res.A16[4]]
    colors = ['b', 'g', 'r', 'c', 'm']
    labels = ["High Income", "High-Medium Income", "Low Income", "Medium Income", "Medium-Low Income"]
    explode = (0.2, 0, 0, 0, 0)
    plt.pie(values, colors=colors, labels=values, explode=explode, counterclock=False, shadow=True)
    plt.title('Correlation between Income and Approval')
    plt.legend(labels, loc=3)
    plt.show()


def print_basic_pie_sex_0_approval(res):
    plt.figure(figsize=(10, 6))
    values = [res.A16[0][0], res.A16[0][1]]
    colors = ['b', 'g']
    labels = ["Sex_0 No_Approval", "Sex_0 Yes_Approval"]
    explode = (0.1, 0.1)
    plt.pie(values, colors=colors, labels=values, explode=explode, counterclock=False, shadow=True)
    plt.title('Correlation between Sex 0 and Approval')
    plt.legend(labels, loc=3)
    plt.show()


def print_basic_pie_sex_1_approval(res):
    plt.figure(figsize=(10, 6))
    values = [res.A16[1][0], res.A16[1][1]]
    colors = ['r', 'c']
    labels = ["Sex_1 No_Approval", "Sex_1 Yes_Approval"]
    explode = (0.1, 0.1)
    plt.pie(values, colors=colors, labels=values, explode=explode, counterclock=False, shadow=True)
    plt.title('Correlation between Sex 1 and Approval')
    plt.legend(labels, loc=3)
    plt.show()


if __name__ == '__main__':
    repair_missing_value_numerical_attribute("A2")
    set_class_age()
    print_basic_histogram_age(dataset.class_Age)
    log_trasformation_age()
    print_basic_histogram_log_age(dataset.class_log_Age)

    set_class_sex()
    print_basic_histogram_sex(dataset.A1)

    repair_missing_value_numerical_attribute("A8")
    set_class_years_of_work()
    print_basic_histogram_years_of_work(dataset.class_Years_of_works)

    repair_missing_value_numerical_attribute("A15")
    print_basic_histogram_income(dataset.A15)

    dataset["class_Income"] = dataset.apply(class_for_income, axis=1)
    print(dataset.head())

    set_class_approval()

    print_sex_positive_approval()
    res = print_sex_correlation()
    print_basic_pie_sex_0_approval(res)
    print_basic_pie_sex_1_approval(res)

    res = print_income_correlation()
    print_basic_pie_income_approval(res)

    print_years_of_work_correlation()

    print_average_age_approval()
    print_average_income_approval()
    print_average_years_of_work_approval()








