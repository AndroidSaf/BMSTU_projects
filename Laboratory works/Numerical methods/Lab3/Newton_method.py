import time as t
import numpy as np
from sympy import symbols, diff


def Newton_method(f, segment, epsilon):
    begin = t.time()
    x = symbols('x')
    dx = diff(f, x)
    x_curr = (segment[0] + segment[1]) / 2
    x_next = x_curr - f.subs(x, x_curr) / dx.subs(x, x_curr)
    i = 1
    while np.abs(x_next - x_curr) > epsilon:
        x_curr = x_next
        x_next = x_curr - f.subs(x, x_curr) / dx.subs(x, x_curr)
        i += 1
    end = t.time()
    return [x_next, i, end - begin]
