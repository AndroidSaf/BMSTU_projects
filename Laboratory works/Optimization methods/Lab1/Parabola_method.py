import time as t
import numpy as np
import Segment_dichotomy_method as f_1


def Parabola_method(f, segment, epsilon):
    begin = t.time()
    a = segment[0]
    b = segment[1]

    while True:
        three_x = np.sort(np.array([np.random.uniform(a - 1, b) for i in range(3)]))

        if f(three_x[1]) > f(three_x[0]) < f(three_x[2]):

            h = 0.00001
            x = three_x[1]
            x_next = x - np.divide(h * (f(x + h) - f(x - h)), 2 * (f(x + h) - 2 * f(x) + f(x - h)))

            while np.abs(f(x_next) - f(x)) > epsilon:
                x = x_next
                x_next = x - np.divide(h * (f(x + h) - f(x - h)), 2 * (f(x + h) - 2 * f(x) + f(x - h)))
        else:
            # Segment dichotomy method
            x = f_1.mean(a, b)
            x_next = f_1.min_f(f, a, b, x)
            a = x_next
            b = x

            if np.abs(f(x_next) - f(x)) < epsilon:
                break
    end = t.time()

    return [f(x_next), end - begin]
