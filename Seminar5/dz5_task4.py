"""
Есть ли статистически значимые различия в среднем росте матерей и
дочерей?
Рост матерей 172, 177, 158, 170, 178,175, 164, 160, 169, 165
Рост взрослых дочерей: 173, 175, 162, 174, 175, 168, 155, 170, 160, 163
"""
import numpy as np
import scipy.stats as stats

mothers = np.array([172, 177, 158, 170, 178, 175, 164, 160, 169, 165])
daughters = np.array([173, 175, 162, 174, 175, 168, 155, 170, 160, 163])

print(stats.ttest_rel(mothers, daughters))

# статистически значимых различий нет для альфа = 0.05
