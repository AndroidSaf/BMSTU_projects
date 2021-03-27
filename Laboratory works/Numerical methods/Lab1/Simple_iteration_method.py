import time as t
import numpy as np
import random as rd


def get_B(A, X):
    return np.dot(A, X)


def d_max(X_1, X_2, n):
    max = 0
    for i in range(n):
        m = np.abs(X_1[i] - X_2[i])
        if m > max:
            max = m
    return max


def diag_max(C, n):
    for i in range(n):
        for j in range(n):
            if i == j:
                C[i, j] = np.random.uniform(10000, 11000)
            else:
                C[i, j] = np.random.uniform(0, 1)
    return C


def Simple_iteration_method(n, iter_q):
    delta_X_array = np.zeros(iter_q)
    time = np.zeros(iter_q)

    for l in range(iter_q):
        begin = t.time()
        A = np.array([np.random.uniform(1, 10) for i in range(n ** 2)]).reshape(n, n)
        X = np.array([np.random.uniform(1, 10) for i in range(n)])
        A = diag_max(A, n)
        B = get_B(A, X)

        begin = t.time()
        epsilon = np.exp(-36)
        A_new = np.zeros((n, n))
        B_new = np.zeros(n)
        C = np.zeros(n)

        for i in range(n):
            B_new[i] = B[i] / A[i, i]
            for j in range(n):
                if i != j:
                    A_new[i, j] = -1 * A[i, j] / A[i, i]

        a_max = a = 0
        for i in range(n):
            for j in range(n):
                a += np.abs(A_new[i, j])
            if a > a_max:
                a_max = a
            a = 0

        X_1 = B_new + np.dot(A_new, C)
        delta = 1
        while delta > np.abs((1 - a_max) * epsilon / a_max):
            X_2 = X_1
            X_1 = B_new + np.dot(A_new, X_2)
            delta = d_max(X_1, X_2, n)
        end = t.time()

        delta_X_array[l] = np.std(X - X_1)
        time[l] = end - begin
    return [str(n) + ' x ' + str(n), iter_q, np.min(delta_X_array), np.max(delta_X_array), np.mean(time)]
