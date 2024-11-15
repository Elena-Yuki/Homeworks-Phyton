import requests
import pandas as pd
import numpy as np

# 1. Использование библиотеки requests
print("Запрос данных с сайта https://lingualeo.com/") # создаем запрос с сайта для иучения иностранных языков 

# оздание и отправка GET-запроса

url = 'https://lingualeo.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Данные успешно получены:")
    print("Первые 200 символов ответа:")
    print(response.text[:300])
else:
    print("Ошибка при запросе данных:", response.status_code)


# 2. Использование библиотеки pandas
print("\nСоздание DataFrame") # создаем  DataFrame из словаря
data = {
    'names': ['Steve', 'Jelco', 'Javier', 'Daria', 'Monica'], # имена студентов
    'age': [28, 29, 26, 33, 31], # озраст студентов
    'scores': [8.9, 7.8, 9.3, 8.8, 7.9], # оценки студентов
    'countries': ['UK', 'Serbia', 'Spain', 'Russia', 'Mexica'] # страны
}

df = pd.DataFrame(data)
print("Первые 5 строк данных:")
print(df.head())

print("\nФильтрация данных по определенному условию")
filtered_df = df[df['scores'] > 7.9]  # Фильтрация по баллу меньше 7.9
print(filtered_df)

print("\nГруппировка данных")
grouped_df = df.groupby('names')['scores'].mean() # производим группировку данных 
print(grouped_df)


#Использование библиотеки numpy

h = np.array([[5, 6, 7],
              [8, 9, 10]])
print(h.shape)  #вывод колличества строк и столбцов

h = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(h)  # вывод таблицы из списков
print(h.shape)   #вывод колличества строк и столбцов

print(np.linspace(0, 20, num=5))  #вывод линейного массива через указанный интервал






