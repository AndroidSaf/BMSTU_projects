import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from scipy.optimize import fsolve


def plot_1(f):
    x = np.arange(-2.0, 6.1, 0.01)
    plt.plot(x, f(x), color='forestgreen')
    plt.axis('square')
    plt.axis([-2, 6, -4, 4])
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title("f(x) = x(x-2)(x-4)")
    plt.grid('on')
    x = sym.symbols('x', real=True)
    ans = sym.solve(sym.Eq(x * (x - 2) * (x - 4), 0), x)
    for i in range(len(ans)):
        plt.scatter(ans[i], f(ans[i]), color='forestgreen')
        plt.text(ans[i] + 0.1, f(ans[i]), '({}, {})'.format(ans[i], f(ans[i])))
    plt.show()
    return 0


def plot_2(f):
    x = np.arange(-8.0, 2.1, 0.01)
    plt.plot(x, f(x), color='orange')
    plt.axis('square')
    plt.axis([-8, 2, -5, 5])
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title("f(x) = e^x + sin(x)")
    plt.grid('on')
    for i in range(3):
        x[i] = fsolve(f, -i * 3)
        x[i] = round(x[i], 3)
        y = int(f(x[i]))
        plt.scatter(x[i], y, color='orange')
        plt.text(x[i] + 0.3, y, '({}, {})'.format(x[i], y))
    plt.show()
    return 0


def plot_3(f):
    x = np.arange(-6.0, 6.1, 0.01)
    plt.plot(x, f(x), color='teal')
    plt.axis('square')
    plt.axis([-1, 1, -1, 1])
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title("f(x) = x^10-2x^9+3x^8-x^7+5x^6+x^5-x^4-x^3+x^2-x")
    plt.grid('on')
    x = sym.symbols('x', real=True)
    ans = sym.solve(sym.Eq(x ** 10 - 2 * x ** 9 + 3 * x ** 8 - x ** 7 + 5 * x ** 6 + x ** 5 - x ** 4 - x ** 3 + x ** 2 - x, 0), x)
    for i in range(len(ans)):
        ans[i] = round(ans[i], 4)
        plt.scatter(ans[i], round(f(ans[i])), color='teal')
        plt.text(ans[i] + 0.05, round(f(ans[i])), '({}, {})'.format(ans[i], round(f(ans[i]))))
    plt.show()
    return 0
