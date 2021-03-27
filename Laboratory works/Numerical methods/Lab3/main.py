from Segment_dichotomy_method import Segment_dichotomy_method
from Secant_method import Secant_method
from Newton_method import Newton_method
from Plots import *
import numpy as np
import pandas as pd
import sympy as sym

data = {'equation values': pd.Series(np.zeros(3),
                                     index=['Segment dichotomy method', 'Secant method',
                                            'Newton method']),
        'iterations': pd.Series(np.zeros(3),
                                index=['Segment dichotomy method', 'Secant method',
                                       'Newton method']),
        'time': pd.Series(np.zeros(3),
                          index=['Segment dichotomy method', 'Secant method',
                                 'Newton method'])}
df = pd.DataFrame(data)

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 3)


def f_1(x):
    return x * (x - 2) * (x - 4)


def f_2(x):
    return np.exp(x) + np.sin(x)


def f_3(x):
    return np.power(x, 10) - 2 * np.power(x, 9) + 3 * np.power(x, 8) - np.power(x, 7) + 5 * np.power(x, 6) \
           + np.power(x, 5) - np.power(x, 4) - np.power(x, 3) + np.power(x, 2) - np.power(x, 1)


f_1_sympy = sym.expand('x * (x - 2) * (x - 4)')
f_2_sympy = sym.expand('exp(x) + sin(x)')
f_3_sympy = sym.expand('x ** 10 - 2 * x ** 9 + 3 * x ** 8 - x ** 7 + 5 * x ** 6 + x ** 5 - x ** 4 - x ** 3 + x ** 2 - x')


names = {
    '1': 'Segment dichotomy method',
    '2': 'Secant method',
    '3': 'Newton method',
}

func_names = {
    '1': f_1,
    '2': f_2,
    '3': f_3
}

func_names_sympy = {
    '1': f_1_sympy,
    '2': f_2_sympy,
    '3': f_3_sympy
}

plot_1(f_1)
plot_2(f_2)
plot_3(f_3)
segment = np.zeros(2)
epsilon = 1e-5

while True:
    print()
    print("Choose function for equation: ")
    print(" 1. y = x(x-2)(x-4)\n", "2. y = e^x + sin(x)\n",
          "3. y = x^10-2x^9+3x^8-x^7+5x^6+x^5-x^4-x^3+x^2-x\n")
    func_number = input()
    segment[0] = float(input("Enter the begining of segment: "))
    segment[1] = float(input("Enter the end of segment: "))

    methods = {
        '1': Segment_dichotomy_method(func_names[func_number], segment, epsilon),
        '2': Secant_method(func_names[func_number], segment, epsilon),
        '3': Newton_method(func_names_sympy[func_number], segment, epsilon),
    }

    while True:
        print("Choose the method:")
        print(" 1. Segment dichotomy method\n", "2. Secant method\n",
              "3. Newton method\n")

        method_number = input("Case: ")
        df.loc[names[method_number]] = methods[method_number]
        print(df, "\n")
        print("Back to menu?")
        k = input()
        if k == 'no':
            break

    print("Want to change data?")
    l = input()
    if l == 'no':
        break
print("Thank you for attention!")
