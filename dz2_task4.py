"""
В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых.
Из каждого ящика вытаскивают случайным образом по два мяча.
Какова вероятность того, что все мячи белые?
Какова вероятность того, что ровно два мяча белые?
Какова вероятность того, что хотя бы один мяч белый?
"""
import numpy as np


def combinations(n, k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))


# а)
# находим количество благоприятных исходов
m = combinations(7, 2) * combinations(9, 2)
# находим общее количество исходов
n = combinations(10, 2) * combinations(11, 2)
# находим необходимую вероятность
p = round(m / n, 4)

# б)
# находим количество благоприятных исходов
m = combinations(7, 2) * combinations(2, 2) + combinations(7, 1) * combinations(3, 1) * combinations(9, 1) * \
    combinations(2, 1) + combinations(3, 2) * combinations(9, 2)
# находим общее количество исходов
n = combinations(10, 2) * combinations(11, 2)
# находим необходимую вероятность
p = round(m / n, 4)

# в)
# находим количество благоприятных исходов  (все мячи чёрные)
m = combinations(3, 2) * combinations(2, 2)
# находим общее количество исходов
n = combinations(10, 2) * combinations(11, 2)
# находим необходимую вероятность вычитая из 1
p = 1 - round(m / n, 4)
