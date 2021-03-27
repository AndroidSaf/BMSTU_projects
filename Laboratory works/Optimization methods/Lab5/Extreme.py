import sympy as sp
import matplotlib.pyplot as plt
import numpy as np


x = sp.symbols('x')
y = sp.Function('y')
euler_equation = sp.Eq(sp.diff(y(x), x, 2) - 6 * x, 0)
solve = sp.dsolve(euler_equation)
print(solve)

x = np.linspace(-1, 1, 100)
y = lambda C1, C2: C1 + C2 * x + np.power(x, 3)

y_0 = y(0, 0)
y_1_p = y(1, 0)
y_2_p = y(2, 0)
y_3_p = y(3, 0)
y_1_m = y(-1, 0)
y_2_m = y(-2, 0)
y_3_m = y(-3, 0)

y0 = y(1, 0)
y1p = y(1, 1)
y2p = y(1, 2)
y3p = y(1, 3)
y1m = y(1, -1)
y2m = y(1, -2)
y3m = y(1, -3)

plt.figure('square')
plt.grid(True)

for i in [y2m, y1m, y0, y1p, y2p]:
    plt.plot(x, i, color='forestgreen')
for i in [y_1_m, y_0, y_1_p, y_2_p, y_3_p]:
    plt.plot(x, i, color='royalblue')
plt.plot(x, y(-1, 0), color='red', linewidth=2)
plt.savefig('D:\Python\one.png')
plt.show()
