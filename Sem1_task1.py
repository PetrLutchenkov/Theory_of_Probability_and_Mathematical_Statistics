"""
В партии 10 делалей. Среди них 3 бракованные. Какова вероятность, что среди 5, взятых на удачу, 4 хорошие детали?
"""
import numpy as np


def combinations(n, k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))


# находим количество благоприятных исходов
m = combinations(3, 1) * combinations(7, 4)
print(m)
# находим общее количество исходов
n = combinations(10, 5)
print(n)
# вычисляем нашу вероятность
p = round(m / n, 3)
print(p)
