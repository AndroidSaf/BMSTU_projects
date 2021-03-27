import numpy as np
import pandas as pd
import Central_rectangle_method as file_1
import Trapeze_method as file_2
import Simson_method as file_3

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 5)

data = {'SymPy Integration': pd.Series(np.ones(3),
                                       index=['Central rectangle method', 'Trapeze method',
                                              'Simson method']),
        'Numerical Integration': pd.Series(np.zeros(3),
                                           index=['Central rectangle method', 'Trapeze method',
                                                  'Simson method']),
        'Precision': pd.Series(np.ones(3),
                               index=['Central rectangle method', 'Trapeze method',
                                      'Simson method']),
        'Time': pd.Series(np.zeros(3),
                          index=['Central rectangle method', 'Trapeze method',
                                 'Simson method'])}
df = pd.DataFrame(data)


def f_1(x):
    return np.power(x, 4) + np.power(x, 3) - np.divide(p, 4) * np.power(x, 2) + 1


def f_2(x):
    return np.divide(np.power(x, 2), p) + np.cos(2 * x) + np.divide(np.pi, 2)


def f_3(x):
    return np.sin(np.divide(p * np.power(x, 2), 8))


l = 'yes'
segment = np.zeros(2)

while l == 'yes':
    print()
    p = 17

    f_name = {
        '1': 'y = x^4 + x^3 + p*x^2/4 + 1',
        '2': 'y = x^2/p + cos(2x) + pi/2',
        '3': 'y = sin(p*x^2/8)'
    }
    print("Your parameter p = 17 ")
    print("Choose your function: ")
    print(" 1. y = x^4 + x^3 + p*x^2/4 + 1\n", "2. y = x^2/p + cos(2x) + pi/2\n", "3. y = sin(p*x^2/8)")
    f_number = input("Function: ")
    segment[0] = float(input("Enter the begining of segment: "))
    segment[1] = float(input("Enter the end of segment: "))
    epsilon = float(input("Enter the epsilon: "))
    k = 'yes'

    functions = {
        '1': f_1,
        '2': f_2,
        '3': f_3
    }

    methods = {
        '1': file_1.Central_rectangle_method(functions[f_number], segment, epsilon),
        '2': file_2.Trapeze_method(functions[f_number], segment, epsilon),
        '3': file_3.Simson_method(functions[f_number], segment, epsilon)
    }

    names = {
        '1': 'Central rectangle method',
        '2': 'Trapeze method',
        '3': 'Simson method'
    }

    while k == 'yes':
        print(
            f'Choose the method to integrate {f_name[f_number]} on segment [{segment[0]}; {segment[1]}] with {epsilon} precision and p = {p}:'.format(
                f_name[f_number], segment[0], segment[1], epsilon, p))
        print(" 1. Central rectangle method\n", "2. Trapeze method\n", "3. Simson method")
        method_number = input("Method: ")
        df.loc[names[method_number]] = methods[method_number]
        print(df, "\n")
        print("Back to menu?")
        k = input()
    print("Want to change function and data?")
    df.to_csv('D:\Python\data.csv')
    df = df.applymap(lambda x: 0)
    l = input()

print("Thank you for attention!")
