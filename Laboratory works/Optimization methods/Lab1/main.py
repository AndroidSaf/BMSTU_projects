import numpy as np
import Segment_dichotomy_method as f_1
import Golden_ratio_method as f_2
import Parabola_method as f_3
import Secant_method as f_4
import Tangents_method as f_5
import pandas as pd
import sympy as sym
import matplotlib.pyplot as plt

data = {'extremum': pd.Series(np.zeros(5),
                              index=['Segment dichotomy method(local)', 'Golden ratio method(local)',
                                     'Parabola method(local/global)',
                                     'Secant method(global)', 'Tangents method(global)']),
        'time': pd.Series(np.zeros(5),
                          index=['Segment dichotomy method(local)', 'Golden ratio method(local)',
                                 'Parabola method(local/global)', 'Secant method(global)',
                                 'Tangents method(global)'])}
df = pd.DataFrame(data)

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 5)


def f(x):
    return np.square(x) + np.divide(16, x)


x = np.arange(-2.005, 5.01, 0.01)
y = f(x)
plt.plot(x, y, color='orange')
plt.axis('square')
plt.axis([0.1, 5, 10, 15])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x) = x ** 2 + 16 / x')
plt.grid('on')
plt.show()
f_sympy = sym.expand('x ** 2 + 16 / x')

segment = np.zeros(2)
l = 'yes'

while l == 'yes':
    print()
    print("Your function: y = x^2 + 16/x")
    segment[0] = float(input("Enter the begining of segment: "))
    segment[1] = float(input("Enter the end of segment: "))
    epsilon = float(input("Enter the epsilon: "))
    k = 'yes'

    methods = {
        '1': f_1.Segment_dichotomy_method(f, segment, epsilon),
        '2': f_2.Golden_ratio_method(f, segment, epsilon),
        '3': f_3.Parabola_method(f, segment, epsilon),
        '4': f_4.Secant_method(f_sympy, segment, epsilon),
        '5': f_5.Tangents_method(f_sympy, segment, epsilon)
    }

    names = {
        '1': 'Segment dichotomy method(local)',
        '2': 'Golden ratio method(local)',
        '3': 'Parabola method(local)',
        '4': 'Secant method(global)',
        '5': 'Tangents method(global)'
    }

    while k == 'yes':
        print(
            f'Choose the method to find global extremum or local on segment [{segment[0]}; {segment[1]}] of your function with {epsilon} precision'.format(
                segment[0], segment[1], epsilon))
        print(" 1. Segment dichotomy method(local)\n", "2. Golden ratio method(local)\n", "3. Parabola method(local/global)\n",
              "4. Secant method(global)\n",
              "5. Tangents method(global)\n")

        method_number = input("Case: ")
        df.loc[names[method_number]] = methods[method_number]
        print(df, "\n")
        print("Back to menu?")
        k = input()

    print("Want to change segment and precision?")
    l = input()

print("Thank you for attention!")
