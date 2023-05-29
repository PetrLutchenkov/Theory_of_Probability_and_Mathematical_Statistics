"""
Даны значения зарплат из выборки выпускников:
100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
Посчитать (желательно без использования статистических методов наподобие std, var, mean):
среднее арифметическое
среднее квадратичное отклонение
смещенную и несмещенную оценки дисперсий для данной выборки.
"""
salaries = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]

# среднее арифметическое
average = sum(salaries) / len(salaries)
print(f'Средрее арифметическое: {average}')

# среднее квадратичное отклонение
squared_residuals = [(salary - average) ** 2 for salary in salaries]
std = (sum(squared_residuals) / len(salaries)) ** (1 / 2)
print(f'Среднее квадратичное отклонение - {round(std, 2)}')

# несмещенная дисперсия
dispersion = sum(squared_residuals) / (len(salaries) - 1)
print(f'Несмещённая дисперсия - {round(dispersion, 2)}')

# смещенная дисперсия
dispersion = sum(squared_residuals) / len(salaries)
print(f'Смещённая дисперсия - {round(dispersion, 2)}')
