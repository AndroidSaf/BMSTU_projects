import time as t
import numpy as np
from scipy.integrate import quad


def Trapeze_method(f, segment, epsilon):
    begin = t.time()
    s = np.divide(f(segment[0]) + f(segment[1]), 2)
    n = int(np.divide(segment[1] - segment[0], epsilon))

    for i in range(1, n):
        s += np.divide(f(segment[0] + i * epsilon) + f(segment[0] + i * epsilon), 2)
    end = t.time()
    I = quad(f, segment[0], segment[1])

    return [I[0], s * epsilon, I[0] - s * epsilon, end - begin]

