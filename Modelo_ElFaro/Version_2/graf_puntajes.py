  
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('puntajes.csv')
p_puntajes = []

N = 0
n = 1
for i in data.itertuples():
    # print(i)
    x = [j for j in i]
    x = x[2:-1]
    suma = sum(x)
    N = len(x)
    promedio_r = suma/N
    # print(x)
    p_puntajes.append(promedio_r)
    n += 1

    # print(x)

rondas = [i for i in range(n-1)]

fig, ax = plt.subplots()
ax.plot(rondas, p_puntajes, 'g')
ax.set(xlabel='Rondas', ylabel='Puntaje(%)', xlim = [0, 110], ylim = [-1, 0.5],
       title='puntaje promedio por Ronda a El Farol')
ax.legend(["puntaje por Ronda"])
ax.grid()

plt.show()