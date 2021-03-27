import time as t
import numpy as np


def Golden_ratio_method(f, segment, epsilon):
    begin = t.time()
    a = segment[0]
    b = segment[1]
    Phi = np.divide(1 + np.sqrt(5), 2)
    x_1 = b - np.divide(b - a, Phi)
    x_2 = a + np.divide(b - a, Phi)

    if f(x_1) > f(x_2):
        a = x_1
    else:
        b = x_2

    while np.abs(b - a) > epsilon:
        x_1 = b - np.divide(b - a, Phi)
        x_2 = a + np.divide(b - a, Phi)
        if f(x_1) > f(x_2):
            a = x_1
        else:
            b = x_2
    end = t.time()

    return [f(np.divide(a + b, 2)), end - begin]
