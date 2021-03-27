import numpy as np
import matplotlib.pyplot as plt


#Drawing stream type phase portrait of linear ODE system
def df_2(x, y):
    return [4*x+2*y, x + 3*y]

X, Y = np.meshgrid(np.linspace(-10, 10, 50), np.linspace(-10, 10, 50))
u, v = np.zeros(X.shape), np.zeros(Y.shape)
n_i, n_j = X.shape

for i in range(n_i):
    for j in range(n_j):
         x_coordinate, y_coordinate = X[i, j], Y[i, j]
         x, y = x_coordinate, y_coordinate
         f_2 = df_2(x, y)
         u[i, j] = f_2[0]
         v[i, j] = f_2[1]

plt.streamplot(X, Y, u, v, color='black', density=2, linewidth=1,  arrowsize=1)
plt.axis('square')
plt.axis([-10, 10, -10, 10])
plt.axis("off")
plt.show()


#Drawing stream type phase portrait of nonlinear ODE system
def df_2(x, y):
    return [np.exp(y) - np.exp(x), np.sqrt(3*x+pow(y,2)) - 2]

X, Y = np.meshgrid(np.linspace(-3, 3, 25), np.linspace(-3, 3, 25))
u, v = np.zeros(X.shape), np.zeros(Y.shape)
n_i, n_j = X.shape

for i in range(n_i):
    for j in range(n_j):
         x_coordinate, y_coordinate = X[i, j], Y[i, j]
         x, y = x_coordinate, y_coordinate
         if x >= -pow(y, 2)/3.0:
                f_2 = df_2(x, y)
                u[i, j] = f_2[0]
                v[i, j] = f_2[1]

plt.streamplot(X, Y, u, v, color='orange', density=3, linewidth=1,  arrowsize=1)
plt.ylabel('y(t)')
plt.xlabel('x(t)')
plt.axis('square')
plt.axis([-3, 3, -3, 3])
plt.show()