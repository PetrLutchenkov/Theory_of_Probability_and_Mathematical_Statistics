"""
Рост взрослого населения города X имеет нормальное распределение,
причем средний рост равен 174 см, а среднее квадратическое отклонение равно 8 см.
посчитайте, какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
1. больше 182 см?
2. больше 190 см?
3. от 166 см до 190 см?
4. от 166 см до 182 см?
5. от 158 см до 190 см?
6. не выше 150 см или не ниже 190 см?
7. не выше 150 см или не ниже 198 см?
8. ниже 166 см?

Задачу можно решить двумя способами: без использования сторонних библиотек (numpy, scipy, pandas и пр.),
а затем проверить себя с помощью встроенных функций
"""
import scipy.stats as stats

Mx = 174
std = 8
Dx = std ** 2

# 1)
z = (182 - Mx) / std
p = 1 - 0.8413
print(f'1) {round(p, 3)}')
p = 1 - stats.norm.cdf(z)
print(round(p, 3))

# 2)
z = (190 - Mx) / std
p = 1 - 0.9772
print(f'2) {round(p, 3)}')
p = 1 - stats.norm.cdf(z)
print(round(p, 3))

# 3)
z1 = (166 - Mx) / std
p1 = 1 - stats.norm.cdf(z1)  # или 1 - 0.1587
z2 = (190 - Mx) / std
p2 = 1 - stats.norm.cdf(z)  # или 1 - 0.9772
p = p1 - p2
print(f'3) {round(p, 3)}')

# 4)
z1 = (166 - Mx) / std
p1 = 1 - stats.norm.cdf(z1)
z2 = (182 - Mx) / std
p2 = 1 - stats.norm.cdf(z2)
p = p1 - p2
print(f'4) {round(p, 3)}')

# 5)
z1 = (158 - Mx) / std
p1 = 1 - stats.norm.cdf(z1)
z2 = (190 - Mx) / std
p2 = 1 - stats.norm.cdf(z2)
p = p1 - p2
print(f'5) {round(p, 3)}')

# 6)
z1 = (150 - Mx) / std
p1 = stats.norm.cdf(z1)
z2 = (190 - Mx) / std
p2 = 1 - stats.norm.cdf(z2)
p = p1 + p2
print(f'6) {round(p, 3)}')

# 7)
z1 = (150 - Mx) / std
p1 = stats.norm.cdf(z1)
z2 = (198 - Mx) / std
p2 = 1 - stats.norm.cdf(z2)
p = p1 + p2
print(f'7) {round(p, 4)}')

# 8)
z = (166 - Mx) / std
p = 0.1587
print(f'8) {round(p, 3)}')
p = stats.norm.cdf(z)
print(round(p, 3))