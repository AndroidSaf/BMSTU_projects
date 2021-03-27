import time as t
from sympy import symbols
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from Secant_method import Secant_method
import seaborn as sns

sns.set()
f = sym.expand('x^2 + 16/x')
segment = [0.2, 0.8]
p_segment = [-1, 1]
dp = 0.1
epsilon = 1e-3
method = 'Secant_method'


def conjugate_function(p_segment, dp, segment, f, epsilon, method='sp'):
    begin = t.time()
    x = symbols('x')
    p = symbols('p', real=True)
    p = np.arange(p_segment[0], p_segment[1] + dp, dp)
    a = [segment[0]] * len(p)
    b = [segment[1]] * len(p)
    epsilon = [epsilon] * len(p)
    obj = -1 * (p * x - f)
    if method == 'Secant_method':
        sup = list(map(Secant_method, obj, a, b, epsilon))
    y = [-1 * item for item in sup]
    plt.plot(p, y, label='linear', color='forestgreen', linestyle='-', linewidth=2)
    plt.axis('square')
    plt.axis([-1, 1, -3, -1])
    plt.legend()
    plt.xlabel('p')
    plt.ylabel('f*(p)')
    plt.grid('on')
    plt.title('Convex conjugate')
    plt.show()
    end = t.time()
    return 0


conjugate_function(p_segment, dp, segment, f, epsilon, method)