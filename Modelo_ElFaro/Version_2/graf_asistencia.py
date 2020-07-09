import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('estrategias.csv')
asistencia = []

N = 0
n = 1
for i in data.itertuples():
    # print(i)
    x = [j for j in i]
    x = x[2:-1]
    N = len(x)
    # print(x)
    asistencia.append(sum(x))
    n += 1

    # print(x)

rondas = [i for i in range(n-1)]
asistencia_2 = [i/N for i in asistencia]

fig, ax = plt.subplots()
ax.plot(rondas, asistencia_2, 'g')
ax.set(xlabel='Rondas', ylabel='Asistencia(%)', xlim = [0, 100], ylim = [0, 1],
       title='Asistencia por Ronda a El Farol')
ax.legend(["Asistencia por Ronda"])
ax.grid()

plt.show()
