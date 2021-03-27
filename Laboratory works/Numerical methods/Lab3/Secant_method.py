import numpy as np
import time as t


def Secant_method(f, segment, epsilon):
    begin = t.time()
    x_prev = segment[0]
    x_curr = segment[1]
    x_next = x_curr - np.divide((x_curr - x_prev) * f(x_curr), f(x_curr) - f(x_prev))
    i = 1
    while np.abs(x_curr - x_prev) > epsilon:
        x_prev = x_curr
        x_curr = x_next
        x_next = x_curr - np.divide((x_curr - x_prev) * f(x_curr), f(x_curr) - f(x_prev))
        i += 1
    end = t.time()
    return [x_next, i, end - begin]
