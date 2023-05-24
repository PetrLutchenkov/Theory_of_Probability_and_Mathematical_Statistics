"""
В ящике находится 10 красных, 5 черных, 5 зеленых шаров. Наудачу вынимают 6 шаров.
Какова вероятность, что вынуты 3 красных, 2 черных, 1 зеленый?
"""
import numpy as np


def combinations(n, k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))

# находим количество благоприятных исходов
m = combinations(10, 3) * combinations(5, 2) * combinations(5, 1)
# находим общее количество исходов
n = combinations(20, 6)
# вычисляем нашу вероятность
P = round(m / n, 3)
print(P)
