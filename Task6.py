import numpy as np;

def SumOfElements(x):
    if a == b:
        z=[m[i][i] for i in range(len(m))]
        return sum(z)
    else: return -1
    
print('Введите размер квадратной матрицы')
a=int(input())
b=int(input())
m = np.random.randint(0, 10, (a, b))
print(m)
k = SumOfElements(a)
if(k == -1): 
    print('Вы ввели размер не квадратной матрицы!')
else: 
    print(k)
print('')