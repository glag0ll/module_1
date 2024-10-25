import ast
import pandas as pd
import numpy as np

data = pd.read_csv("raw_dataset.csv")
columns = [
    "experience",
    "employment",
    "salary_min",
    "salary_max",
    "area"
]

experience = {
    "Нет опыта": 0,
    "От 1 года до 3 лет": 1,
    "От 3 до 6 лет": 2,
    "Более 6 лет": 3
}

employements = {

    "Полная занятость": 0,
    "Частичная занятость": 1,
    "Проектная работа": 2,
    "Волонтерство": 3,
    "Стажировка": 4

}

data["area"] = data["area"].map(lambda city: ast.literal_eval(city)["name"])
data["experience"] = data["experience"].map(lambda experience: ast.literal_eval(experience)["name"])
data["employment"] = data["employment"].map(lambda employment: ast.literal_eval(employment)["name"])

data["salary_min"] = data["salary"].map(
    lambda salary_min: ast.literal_eval(salary_min)["from"]
    if ast.literal_eval(salary_min)["from"] is not None
    else ast.literal_eval(salary_min)["to"]
)
data["salary_max"] = data["salary"].map(
    lambda salary_max: ast.literal_eval(salary_max)["to"]
    if ast.literal_eval(salary_max)["to"] is not None
    else ast.literal_eval(salary_max)["from"]
)

data["experience"] = data["experience"].map(lambda experience: schedule[experience])
data["employment"] = data["employment"].map(lambda employment: employements[employment])

data[columns].to_csv("cleared.csv")