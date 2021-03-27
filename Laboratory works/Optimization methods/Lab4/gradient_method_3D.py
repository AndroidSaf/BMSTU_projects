import torch
import warnings
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time


warnings.filterwarnings('ignore')
matplotlib.use("TkAgg")

def golden_ratio(x, y, grad_x, grad_y):
    a, b, Phi = 0, 1, np.divide(1 + np.sqrt(5), 2)

    while True:
        lambda_1 = b - np.divide(b - a, Phi)
        lambda_2 = a + np.divide(b - a, Phi)
        if f(x - lambda_1 * grad_x, y - lambda_1 * grad_y) > f(x - lambda_2 * grad_x, y - lambda_2 * grad_y):
            a = lambda_1
        else:
            b = lambda_2
        if np.abs(lambda_1 - lambda_2) < 0.001:
            break
    return np.divide(lambda_1 + lambda_2, 2)

begin = time.time()
x = torch.tensor(3., requires_grad=True)
y = torch.tensor(2., requires_grad=True)
x_value = x.detach().numpy()
y_value = y.detach().numpy()
iterations = 1

f = lambda x, y: (x ** 2 + 2 * y ** 2 + 1) ** 2 + x - torch.log(1 + x ** 2 + 2 * x * y + 3 * y ** 2)

while True:
    f(x, y).backward()
    with torch.no_grad():
        f_1 = f(x, y)
        grad_x = x.grad
        grad_y = y.grad
        lambda_ = golden_ratio(x, y, grad_x, grad_y)
        x -= grad_x * lambda_
        y -= grad_y * lambda_
        f_2 = f(x, y)
        x_value = np.append(x_value, [x.numpy()])
        y_value = np.append(y_value, [y.numpy()])
        x.grad.zero_()
        y.grad.zero_()
        iterations += 1
    if torch.abs(f_2 - f_1) < 0.001:
        break

end = time.time()
print(f'({x};{y})'.format(x, y))
print(f(x, y))
print(iterations)
print(end - begin)

f_plot = lambda x, y: (x ** 2 + 2 * y ** 2 + 1) ** 2 + x - np.log(1 + x ** 2 + 2 * x * y + 3 * y ** 2)

color = 'summer'
x, y = np.mgrid[-3:3.1:50j, -3:3.1:50j]
z = f_plot(x, y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap=color)
ax.view_init(30, 20)
plt.show()

x, y = np.mgrid[-3:3.1:50j, -3:3.1:50j]
C = plt.contour(x, y, z, 10, colors='khaki')
plt.contourf(x, y, z, 10, cmap=color)
plt.clabel(C, fontsize=8)
plt.colorbar()

x_value = np.insert(x_value, 0, 3.)
y_value = np.insert(y_value, 0, 2.)
plt.plot(x_value, y_value, marker='o', markersize=5, markerfacecolor='brown', lw=1, c='brown')
plt.axis('square')
plt.show()