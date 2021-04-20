import numpy as np

def СyclicShift(a):
    b = a[k:]+a[:k]
    return b

a = [1, 2, 3, 4, 5]  
print (a) # вывод Массива
print('Введите  число, на которое сместить массив: \t')
k = int(input())
print(СyclicShift(a))
print('')