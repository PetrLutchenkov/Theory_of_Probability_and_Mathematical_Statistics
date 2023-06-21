"""
Измерены значения IQ выборки студентов,
обучающихся в местных технических вузах:
131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
Известно, что в генеральной совокупности IQ распределен нормально.
Найдите доверительный интервал для математического ожидания с надежностью 0.95.
"""
import numpy as np
import scipy.stats as stats

a = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
# среднее арифметическое выборки
x_1 = np.mean(a)
# несмещённая дисперсия
D = np.var(a, ddof=1)
# доверительный интервал
t1 = stats.t.ppf(0.975, len(a) - 1)
x = [round(x_1 - t1 * np.sqrt(D / 10), 2), round(x_1 + t1 * np.sqrt(D / 10), 2)]
print(f'Доверительный интервал для математического ожидания с надежностью 0.95 {x}')
