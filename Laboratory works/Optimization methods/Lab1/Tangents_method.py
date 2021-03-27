import time as t
import numpy as np
from sympy import symbols, diff


def Tangents_method(f, segment, epsilon):
    begin = t.time()
    x = symbols('x')
    dx = diff(f, x)
    dxx = diff(dx, x)
    x0 = (segment[0] + segment[1]) / 2
    ch = 0
    n = 10
    while True:
        x1 = x0 - dx.subs(x, x0) / dxx.subs(x, x0)
        d = np.abs(x1 - x0)
        x0 = x1
        ch += 1
        if d < epsilon:
            break
    x_min = x1
    end = t.time()
    return [f.subs(x, x_min), end - begin]
