import time as t
import numpy as np


def mean(a, b):
    return (a + b) / 2


def min_f(f, a, b, x):
    if np.abs(f(a) - f(x)) < np.abs(f(b) - f(x)):
        return a
    else:
        return b


def Segment_dichotomy_method(f, segment, epsilon):
    begin = t.time()
    a = segment[0]
    b = segment[1]
    x = mean(a, b)
    x_next = min_f(f, a, b, x)

    while np.abs(f(x_next) - f(x)) > epsilon:
        a = x_next
        b = x
        x = mean(a, b)
        x_next = min_f(f, a, b, x)
    end = t.time()

    return [f(x), end - begin]