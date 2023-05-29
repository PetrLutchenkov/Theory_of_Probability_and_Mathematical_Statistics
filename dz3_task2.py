"""
В первом ящике находится 8 мячей, из которых 5 - белые.
Во втором ящике - 12 мячей, из которых 5 белых.
Из первого ящика вытаскивают случайным образом два мяча, из второго - 4 мяча.
Какова вероятность того, что 3 мяча белые?
"""
import numpy as np


def combinations(n, k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))


# находим количество благоприятных исходов
m = combinations(5, 1) * combinations(3, 1) * combinations(5, 2) * combinations(7, 2) \
    + combinations(3, 2) * combinations(5, 3) * combinations(7, 1) \
    + combinations(5, 2) * combinations(5, 1) * combinations(7, 3)
# находим общее количество исходов
n = combinations(8, 2) * combinations(12, 4)
# вычисляем нашу вероятность
p = round(m / n, 3)
print(p)
