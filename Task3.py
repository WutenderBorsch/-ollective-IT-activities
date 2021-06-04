import numpy as np

def СyclicShift(a):
    return a[k:]+a[:k]

a = [1, 2, 3, 4, 5]  
print (a) # вывод Массива
print('Введите  число, на которое сместить массив: \t')
k = int(input())
print(СyclicShift(a))
print('')
