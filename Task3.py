import numpy as np

a = [1, 2, 3, 4, 5]  
print (a) # вывод Массива
print('Введите  число, на которое сместить массив: \t')
k = int(input())
b = a[k:]+a[:k]
print(b)