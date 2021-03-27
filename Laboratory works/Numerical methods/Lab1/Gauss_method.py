import time as t
import numpy as np


def get_B(A, X):
    return np.dot(A, X)


def Gauss_method(n, iter_q):
    delta_X_array = np.zeros(iter_q)
    time = np.zeros(iter_q)

    for l in range(iter_q):
        begin = t.time()
        A = np.array([np.random.uniform(1, 10) for i in range(n ** 2)]).reshape(n, n)
        X = np.array([np.random.uniform(1, 10) for i in range(n)])
        B = get_B(A, X)

        for k in range(n - 1):
            for i in range(k + 1, n):
                b = A[i, k] / A[k, k]
                for j in range(k, n):
                    A[k, j] *= b
                B[k] *= b
                for j in range(k, n):
                    A[i, j] -= A[k, j]
                B[i] -= B[k]

        k = n - 1
        while k > 0:
            i = k - 1
            while i >= 0:
                b = A[i, k] / A[k, k]
                j = k
                while j >= 0:
                    A[k, j] *= b
                    j -= 1
                B[k] *= b
                j = k
                while j >= 0:
                    A[i, j] -= A[k, j]
                    j -= 1
                B[i] -= B[k]
                i -= 1
            k -= 1

        for i in range(n):
            for j in range(n):
                if i != j:
                    A[i, j] = 0
                else:
                    B[i] /= A[i, j]
                    A[i, j] /= A[i, j]
        new_X = B
        end = t.time()

        delta_X_array[l] = np.std(X - new_X)
        time[l] = end - begin
    return [str(n) + ' x ' + str(n), iter_q, np.min(delta_X_array), np.max(delta_X_array), np.mean(time)]
