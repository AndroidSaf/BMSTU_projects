import time as t
import numpy as np


def get_B(A, X):
    return np.dot(A, X)


def three_diag_matrix(C, n):
    for i in range(n):
        for j in range(n):
            if i == j:
                C[i, j] = np.random.uniform(1, 10)
            elif np.abs(i - j) == 1:
                C[i, j] = np.random.uniform(1, 10)
    return C


def Sweep_method(n, iter_q):
    delta_X_array = np.zeros(iter_q)
    time = np.zeros(iter_q)
    C = np.zeros(n ** 2).reshape(n, n)

    for l in range(iter_q):
        begin = t.time()
        X = np.array([np.random.uniform(1, 10) for i in range(n)])
        A = three_diag_matrix(C, n)
        B = get_B(A, X)

        alpha = np.zeros(n - 1)
        beta = np.zeros(n)
        A_two_diag = np.eye(n)
        alpha[0] = -A[0, 1] / A[0, 0]
        beta[0] = B[0] / A[0, 0]
        A_two_diag[0, 1] = alpha[0]
        for i in range(n - 1):
            for j in range(n - 1):
                if j - i == 1:
                    alpha[i + 1] = -A[i + 1, j + 1] / (A[i + 1, i + 1] + A[j, i] * alpha[i])
                    A_two_diag[i + 1, j + 1] = alpha[i + 1]

        for i in range(n):
            for j in range(n):
                if j - i == 1:
                    beta[i + 1] = (B[i + 1] - A[j, i] * beta[i]) / (A[i + 1, i + 1] + A[j, i] * alpha[i])

        k = n - 1
        while k > 0:
            beta[k - 1] += beta[k] * A_two_diag[k - 1, k]
            A_two_diag[k - 1, k] -= A_two_diag[k, k] * A_two_diag[k - 1, k]
            k -= 1
        end = t.time()

        delta_X_array[l] = np.std(X - beta)
        time[l] = end - begin
    return [str(n) + ' x ' + str(n), iter_q, np.min(delta_X_array), np.max(delta_X_array), np.mean(time)]
