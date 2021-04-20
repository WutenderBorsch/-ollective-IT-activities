import numpy as np;

print('Введите размер квадратной матрицы')
a=int(input())
b=int(input())
m = np.random.randint(0, 10, (a, b))
if a == b:
    z=[m[i][i] for i in range(len(m))]
    print(m)
    print(sum(z))
else: 
    print('Вы ввели размер не квадратной матрицы!')

