import time as t
import numpy as np
from sympy import symbols, diff


def Secant_method(f_sym, a, b, epsilon):
    begin = t.time()
    x = symbols('x')
    dx = diff(f_sym, x)
    ch = 0
    x0 = (a + b) / 2
    x1 = x0 + 2 * epsilon
    while True:
        x2 = x1 - dx.subs(x, x1) * (x1 - x0) / (dx.subs(x, x1) - dx.subs(x, x0))
        d = np.abs(x1 - x0)
        x0 = x1
        x1 = x2
        ch += 1
        if d < epsilon:
            break
    x_min = x2
    end = t.time()
    return x_min
