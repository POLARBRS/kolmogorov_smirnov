import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


numeros_aleatorios = np.random.rand(100)



resultado_ks = stats.kstest(numeros_aleatorios, 'uniform')


print(f'Estadístico D de Kolmogorov-Smirnov: {resultado_ks.statistic}')
print(f'Valor p: {resultado_ks.pvalue}')


plt.hist(numeros_aleatorios, bins=10, density=True, alpha=0.6, color='g')
plt.title('Histograma de números aleatorios uniformes')
plt.show()
