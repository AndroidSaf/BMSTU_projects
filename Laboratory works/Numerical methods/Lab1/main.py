import numpy as np
import pandas as pd
import Gauss_method as file_1
import Sweep_method as file_2
import Simple_iteration_method as file_3

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 5)

data = {'slay dimension': pd.Series(np.zeros(5),
                                    index=['1', '2',
                                           '3', '4', '5']),
        'sweep methods quantity': pd.Series(np.zeros(5),
                                            index=['1', '2',
                                                   '3', '4', '5']),
        'delta X_min': pd.Series(np.zeros(5),
                                 index=['1', '2',
                                        '3', '4', '5']),
        'delta X_max': pd.Series(np.zeros(5),
                                 index=['1', '2',
                                        '3', '4', '5']),
        'time': pd.Series(np.zeros(5),
                          index=['1', '2',
                                 '3', '4', '5'])}
df = pd.DataFrame(data)

f_name = {
    '1': 'Gauss method',
    '2': 'Sweep method',
    '3': 'Simple iteration method'
}

dim_sizes = {
    '1': 5,
    '2': 10,
    '3': 50,
    '4': 100,
    '5': 1000
}

iter_q = [10, 10, 10, 10, 2]

while True:

    print("Choose the method to solve SLAY:")
    print(" 1. Gauss method\n", "2. Sweep method\n", "3. Simple iteration method")
    numb = input()

    while True:
        print("Choose SLAY dimension:")
        print(" 1. 5 x 5\n", "2. 10 x 10\n", "3. 50 x 50\n", "4. 100 x 100\n", "5. 1000 x 1000\n")
        dim = input()

        methods = {
            '1': file_1.Gauss_method(dim_sizes[dim], iter_q[int(dim) - 1]),
            '2': file_2.Sweep_method(dim_sizes[dim], iter_q[int(dim) - 1]),
            '3': file_3.Simple_iteration_method(dim_sizes[dim], iter_q[int(dim) - 1])
        }

        df.loc[dim] = methods[numb]
        print(df, "\n")
        print("Want to change dimension?")
        k = input()
        if k != 'yes':
            break

    print("Want to change method?")
    df.to_csv('D:\Python\data_clay.csv')
    df = df.applymap(lambda x: 0)
    l = input()
    if l != 'yes':
        break

print("Thank you for attention!")
