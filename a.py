import numpy as np

def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100


def lin(x): 
    return 5*x + 40



array = [5,6,7,8,9]

array_y = [45,76,78,87,79]


array_Res = []

for e in array: 
    array_Res.append(lin(e))

print(mean_absolute_percentage_error(array_y,array_Res))