import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import warnings
import seaborn as sns
from pylab import rcParams
from scipy.interpolate import CubicSpline

matplotlib.use("TkAgg")
sns.set()
rcParams['figure.figsize'] = 8, 8
warnings.filterwarnings('ignore')
fig, ax = plt.subplots()

f = lambda x: np.sqrt(2 * x + 1) - np.sin(5 * x - np.divide(np.pi, 6))

n = 20
a = 0
b = 5
x = [a]
y = [f(a)]
begin = 0
end = 5

for i in range(1, n + 1):
    iks = a + i * (b - a) / n
    x.append(iks)
    y.append(f(iks))

cs = CubicSpline(x, y)

diff = []
for i in range(n-1):
    z = (begin + ((end - begin) / (n-1))/2 + (end - begin) / (n-1) * i)
    diff.append(cs(z) - f(z))

max = np.max(np.abs(diff))
rmse = np.std(diff)
print(diff)
print(rmse)
print(max)

t = np.linspace(a - 0.2, b + 0.2, 300)
f1, = plt.plot(t, f(t), color='orange')
plt.scatter(x, y, color='forestgreen')
f2, = plt.plot(t, cs(t), color='forestgreen')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

