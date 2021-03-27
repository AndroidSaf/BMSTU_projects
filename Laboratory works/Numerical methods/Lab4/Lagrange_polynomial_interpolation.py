import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import warnings
import seaborn as sns
from pylab import rcParams
import time

matplotlib.use("TkAgg")
sns.set()
rcParams['figure.figsize'] = 8, 8
warnings.filterwarnings('ignore')
fig, ax = plt.subplots()

f = lambda x: np.sqrt(2 * x + 1) - np.sin(5 * x - np.divide(np.pi, 6))
x = np.linspace(0, 5, 6)

x_n = np.zeros(len(x) - 1)
for i in range(len(x) - 1):
    x_n[i] = (x[i] + x[i + 1]) / 2

y = f(x)


def Lagrange(x, y, t):
    z = 0
    for j in range(len(y)):
        p1 = 1
        p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 *= 1
                p2 *= 1
            else:
                p1 *= (t - x[i])
                p2 *= (x[j] - x[i])
        z += y[j] * p1 / p2
    return z


xnew = np.linspace(0, 5, 300)
begin = time.time()
ynew = [Lagrange(x, y, i) for i in xnew]
end = time.time()

f_1, = ax.plot(xnew, f(xnew), color='orange', label='Original function')
plt.scatter(x, y, color='teal')
f_2, = ax.plot(xnew, ynew, color='teal', label='Lagrange interpolation')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

y_n = f(x_n)
y_n_L = [Lagrange(x, y, i) for i in x_n]
d_y = y_n_L - y_n
rmse = np.std(d_y)
max = np.max(np.abs(d_y))
print(d_y)
print(rmse)
print(max)
print(end - begin)
