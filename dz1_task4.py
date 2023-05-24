"""
В лотерее 100 билетов. Из них 2 выигрышных.
Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?
"""
import numpy as np


def combinations(n, k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))


# аналогично решаем и эту задачу)
m = combinations(2, 2)
n = combinations(100, 2)
p = round(m / n, 4)
print(p)
