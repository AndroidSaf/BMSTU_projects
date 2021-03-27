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


dy = lambda x, y: x + 0.25 * y ** 2

x_0 = 0
y_0 = 1
b = x_0 + 0.5
h = 0.05
n = round(abs(b - x_0) / h)


def Runge_Kutta(x_0, y_0, b, h):
    x_table = [x_0]
    y_table = [y_0]
    x = x_0
    y = y_0
    n = round(abs(b - x_0) / h)

    for i in range(1, n + 1):
        k_1 = dy(x, y) * h
        k_2 = dy((x + h / 2), (y + k_1 / 2)) * h
        k_3 = dy((x + h / 2), (y + k_2 / 2)) * h
        k_4 = dy((x + h), (y + k_3)) * h
        y += (k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6
        y_table.append(y)
        x += h
        x_table.append(x)
    return x_table, y_table


def Euler(x_0, y_0, b, h):
    x_table = [x_0]
    y_table = [y_0]
    x = x_0
    y = y_0
    n = round(abs(b - x_0) / h)

    for i in range(1, n + 1):
        y += dy(x, y) * h
        y_table.append(y)
        x += h
        x_table.append(x)
    return x_table, y_table


x = np.linspace(x_0 - 0.2, y_0 + 0.2, 100)

x_runge, y_runge = Runge_Kutta(x_0, y_0, b, h)
_, y_doubled_runge = Runge_Kutta(x_0, y_0, b, h / 2)
#print(y_runge)

x_euler, y_euler = Euler(x_0, y_0, b, h)
_, y_doubled_euler = Euler(x_0, y_0, b, h / 2)
#print(y_euler)

y_r = np.array(y_runge)
y_e = np.array(y_euler)
print(np.abs(y_r - y_e))
print(np.std(np.abs(y_r - y_e)))

runge_error = []
for i in range(len(y_runge)):
    runge_error.append(abs(y_doubled_runge[2 * i] - y_runge[i]))
error_r = max(runge_error)
print(error_r / 15)

euler_error = []
for i in range(len(y_euler)):
    euler_error.append(abs(y_doubled_euler[2 * i] - y_euler[i]))
error_e = max(euler_error)
print(error_e)

marker_style = dict(markersize=8)
marker_style.update(markeredgecolor="None", markersize=15)
marker = "$\u266B$"
f1, = ax.plot(x_runge, y_runge, marker=marker, **marker_style,
              label='Runge-Kutta method', color='rebeccapurple')
f2, = ax.plot(x_euler, y_euler, marker=marker, **marker_style,
              label='Euler method', color='gold')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
