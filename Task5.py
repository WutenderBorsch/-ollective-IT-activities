import numpy as np
import math


def EuclideanDistance(a, b):
    diff = [(a[i] - b[i])**2 for i in range(len(a))]
    return math.sqrt(sum(diff))
    
print("Введите размер матрицы")
n = int(input())
a = np.random.randint(0,10,(n))
b = np.random.randint(0,10,(n))
print(a, '\n', b)
print(EuclideanDistance(a,b))
print('')
