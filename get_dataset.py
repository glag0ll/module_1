import requests
import pandas as pd


params = {
    "page": 0,
    "per_page": 100,
    "text": "bi",
    "area": "113",
    "currency": "RUR",
    "date_from": "2024-07-22",
    "only_with_salary": True
}

base_url = "https://api.hh.ru/vacancies"

result = requests.get(base_url, params).json()

vacancies = []
vacancies.extend(result["items"])

for i in range(1, result["pages"]):
    params["page"] += 1
    result = requests.get(base_url, params).json()
    vacancies.extend(result["items"])

data = pd.DataFrame.from_dict(vacancies)

data.info()

columns = [
    "area",
    "salary",
    "schedule",
    "experience",
    "employment"
]

data = data[columns]


data.to_csv("raw_dataset.csv")