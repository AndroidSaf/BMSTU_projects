import time as t
import numpy as np
from scipy.integrate import quad


def Simson_method(f, segment, epsilon):
    begin = t.time()
    n = int(np.divide(segment[1] - segment[0], epsilon))
    s = 0
    x = segment[0] + epsilon

    for i in range(1, int(n / 2) + 1):
        s += 4 * f(x)
        x += 2 * epsilon

    x = segment[0] + 2 * epsilon
    for i in range(1, int(n / 2)):
        s += 2 * f(x)
        x += 2 * epsilon
    s_n = (epsilon / 3) * (f(segment[0]) + f(segment[1]) + s)
    end = t.time()
    I = quad(f, segment[0], segment[1])

    return [I[0], s_n, I[0] - s_n, end - begin]
