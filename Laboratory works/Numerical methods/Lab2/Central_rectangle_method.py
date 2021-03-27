import time as t
import numpy as np
from scipy.integrate import quad


def Central_rectangle_method(f, segment, epsilon):
    begin = t.time()
    s = 0
    n = int(np.divide(segment[1] - segment[0], epsilon))

    for i in range(n):
        s += f(segment[0] + epsilon * i + epsilon / 2)
    end = t.time()
    I = quad(f, segment[0], segment[1])

    return [I[0], s * epsilon, I[0] - s * epsilon, end - begin]
