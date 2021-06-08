import numpy as np;

def SumOfElements(x):
    n, m = x.shape
    if n == m:
        z=[x[i][i] for i in range(n)]
        return sum(z)
    else: return -1
    
print('Введите размер квадратной матрицы')
n=int(input())
m=int(input())
arr = np.random.randint(0, 10, (n, m))
print(arr)
k = SumOfElements(arr)
if(k == -1): 
    print('Вы ввели размер не квадратной матрицы!')
else: 
    print(k)
print('')
