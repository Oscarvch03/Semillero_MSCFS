  
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('politicas.csv')

pol0 = []
pol1 = []
pol2 = []
pol3 = []
pol4 = []
pol5 = []
pol6 = []
pol7 = []

c0 = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0

N = 0
n = 1
for i in data.itertuples():
    for k in range(2, len(i) - 1):
        if i[k] == 0:
            c0 += 1
        if i[k] == 1:
            c1 += 1
        if i[k] == 2:
            c2 += 1
        if i[k] == 3:
            c3 += 1
        if i[k] == 4:
            c4 += 1
        if i[k] == 5:
            c5 += 1
        if i[k] == 6:
            c6 += 1
        if i[k] == 7:
            c7 += 1
    pol0.append(c0)
    pol1.append(c1)
    pol2.append(c2)
    pol3.append(c3)
    pol4.append(c4)
    pol5.append(c5)
    pol6.append(c6)
    pol7.append(c7)
    c0 = 0
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    c7 = 0
    n += 1

rondas = [i for i in range(n-1)]

fig, ax = plt.subplots()
ax.plot(pol0)
ax.plot(pol1)
ax.plot(pol2)
ax.plot(pol3)
ax.plot(pol4)
ax.plot(pol5)
ax.plot(pol6)
ax.plot(pol7)
ax.set(xlabel='Rondas', ylabel='politicas', xlim = [0, 100], ylim = [0, 55],
       title='Uso de politicas por ronda')
ax.legend(["politica 0", "politica 1", "politica 2", "politica 3", "politica 4", 
           "politica 5", "politica 6", "politica 7"])
ax.grid()

plt.show()