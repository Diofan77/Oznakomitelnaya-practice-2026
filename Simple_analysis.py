# Индивидуальное задание «SimpleAnalysis» 
# Язык: Python 
# Библиотеки: math, matplotlib, pandas, numpy 

import math 
import random 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

# 1. Генерация данных 

# Генерируем 1000 случайных целых чисел 
numbers = np.random.randint(-10000, 10001, 1000)
 
# Формируем Series 
series = pd.Series(numbers) 

# 2. Расчет числовых характеристик 
 
# Минимальное значение 
min_value = series.min()
 
# Максимальное значение 
max_value = series.max()
 
# Сумма чисел 
sum_value = series.sum()
 
# Среднеквадратическое отклонение 
std_value = series.std()
 
# Количество повторяющихся значений 
duplicates_count = series.duplicated().sum()
 
# 3. Вывод результатов в консоль  

print("АНАЛИЗ ДАННЫХ SERIES") 
print("-" * 40) 
print(f"Минимальное значение: {min_value}") 
print(f"Максимальное значение: {max_value}") 
print(f"Сумма всех чисел: {sum_value}") 
print(f"Среднеквадратическое отклонение: {std_value:.2f}") 
print(f"Количество повторяющихся значений: {duplicates_count}")
 
# 4. Визуализация исходных данных
  
# Линейный график 
plt.figure(figsize=(12, 5)) 
plt.plot(series) 
plt.title("Линейный график исходных данных") 
plt.xlabel("Индекс") 
plt.ylabel("Значение") 
plt.grid(True) 
plt.show() 

# 5. Построение гистограммы 

# Округление до сотен  
rounded_series = series.apply(lambda x: int(round(x, -2))) 
plt.figure(figsize=(12, 5)) 
plt.hist(rounded_series, bins=30) 
plt.title("Гистограмма данных (округление до сотен)") 
plt.xlabel("Значение") 
plt.ylabel("Частота") 
plt.grid(True) 
plt.show() 

# 6. Создание DataFrame 

# Сортировка по возрастанию 
sorted_asc = series.sort_values().reset_index(drop=True) 

# Сортировка по убыванию 
sorted_desc = series.sort_values(ascending=False).reset_index(drop=True)
 
# Формирование DataFrame 
df = pd.DataFrame({ 'Original': series, 'Sorted_Ascending': sorted_asc, 'Sorted_Descending': sorted_desc })

# Сохранение в формате CSV
df.to_csv('data.csv', index=False)

# Вывод первых строк DataFrame
print("\nDATAFRAME:") 
print(df.head())
 
# 7. Визуализация отсортированных данных 
 
plt.figure(figsize=(12, 5)) 
plt.plot(sorted_asc, label='По возрастанию') 
plt.plot(sorted_desc, label='По убыванию') 
plt.title("Сравнение отсортированных данных") 
plt.xlabel("Индекс") 
plt.ylabel("Значение") 
plt.legend() 
plt.grid(True) 
plt.show()






