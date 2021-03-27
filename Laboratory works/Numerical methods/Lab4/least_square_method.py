import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import warnings
import seaborn as sns
from pylab import rcParams

matplotlib.use("TkAgg")
sns.set()
rcParams['figure.figsize'] = 8, 8
warnings.filterwarnings('ignore')
fig, ax = plt.subplots()

f = lambda x: np.sqrt(2 * x + 1) - np.sin(5 * x - np.divide(np.pi, 6))

x = np.linspace(0, 5, 20)
y = f(x)
power = 3

x_n = np.zeros(len(x) - 1)
for i in range(len(x) - 1):
    x_n[i] = (x[i] + x[i + 1]) / 2

A = np.reshape(np.zeros(power ** 2), (power, power))
B = np.zeros(power)

for i in range(power):
    for j in range(power):
        A[i, j] = np.sum(np.power(x, i + j))
    B[i] = np.sum(np.dot(np.power(x, i), y))

solve = np.linalg.solve(A, B)

MNK_function = lambda x: solve[0] + solve[1] * x + solve[2] * x ** 2 #+ solve[3] * x ** 3

x_plot = np.linspace(0, 5, 300)
f_1, = ax.plot(x_plot, f(x_plot), color='tab:orange', label='Original function')
plt.scatter(x, y, color='forestgreen')
f_2, = ax.plot(x_plot, MNK_function(x_plot), color='forestgreen', label='Quadratic function')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

y_n = f(x_n)
y_n_MNK = MNK_function(x_n)
d_y = y_n_MNK - y_n
rmse = np.std(d_y)
max = np.max(np.abs(d_y))
print(solve)
print(d_y)
print(rmse)
print(max)
