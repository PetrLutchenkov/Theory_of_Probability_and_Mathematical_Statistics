"""
Исследовалось влияние препарата на уровень давления пациентов. Сначала
измерялось давление до приема препарата, потом через 10 минут и через 30 минут. Есть
ли статистически значимые различия между измерениями давления? В выборках не соблюдается условие нормальности.
1е измерение до приема препарата: 150, 160, 165, 145, 155
2е измерение через 10 минут: 140, 155, 150, 130, 135
3е измерение через 30 минут: 130, 130, 120, 130, 125
Сравните 1 и 2 е измерения, предполагая, что 3го измерения через 30 минут не было. Есть
ли статистически значимые различия между измерениями давления?
"""
import numpy as np
import scipy.stats as stats

before = np.array([150, 160, 165, 145, 155])
after_10_min = np.array([140, 155, 150, 130, 135])
after_30_min = np.array([130, 130, 120, 130, 125])
print(stats.friedmanchisquare(before, after_10_min, after_30_min))
# даже при уровне статистической значимости 0.01 наблюдаются статистически значимые различия между измерениями
# отвергаем нулевую теорию. Препарат снижает уровень давления

print(stats.wilcoxon(before, after_10_min))
# при уровне альфа = 0.05 не наблюдаются статистически значимые различия. Нулевая теория не отвергается