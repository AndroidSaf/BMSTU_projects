import numpy as np
import time as t


def f(x):
    return x * (x - 2) * (x - 4)


def mean(a, b):
    return (a + b) / 2


def min_f(f, a, b, x):
    if f(a) * f(x) < 0:
        return a
    elif f(b) * f(x) < 0:
        return b


def Segment_dichotomy_method(f, segment, epsilon):
    begin = t.time()
    a = segment[0]
    b = segment[1]
    x = mean(a, b)
    x_next = min_f(f, a, b, x)
    i = 1

    while np.abs(f(x_next) - f(x)) > 2 * epsilon:
        a = x_next
        b = x
        x = mean(a, b)
        x_next = min_f(f, a, b, x)
        i += 1
    end = t.time()

    return [x, i, end - begin]
