import numpy as np;


def SumOfElements(x):
    if n == m:
        z=[x[i][i] for i in range(n)]
        return sum(z)
    else: return -1
    

print('Введите размер квадратной матрицы')
n=int(input())
m=int(input())
a = np.random.randint(0, 10, (n, m))
print(a)
k = SumOfElements(a)
if(k == -1): 
    print('Вы ввели размер не квадратной матрицы!')
else: 
    print(k)
print('')