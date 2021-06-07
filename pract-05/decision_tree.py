import numpy as np
import math

NOT_FIT = 1         # кандидатка не подходит
FIT = 2             # кандидатка подходит

NUMERICAL = 0       # параметр числовой
CATEGORICAL = 1     # параметр категориальный


def decision_tree(X, Y, scale, level=0):
    
    if len(np.unique(Y)) == 1:
        print('class = %d' % Y[0])
        return
    print('')
    
    m, n = X.shape  # количество признаков и примеров
    
    # энтропия до разбиения
    info = Info(Y)

    gain = []
    thresholds = np.zeros(n)

    # цикл вычисления информационного выигрыша
    # по каждому столбцу выборки
    for i in range(n):

        if scale[i] == CATEGORICAL:   # категориальный признак
            
         info_s = 0
            
         tn = len(np.unique(X[:, i]))
         u = np.unique(X[:, i])       #уникальные значения T
         for j in range(tn):
             indx = np.where(X[:, i] == u[j]) #индексы элементов подмножства
             Tj = Y[indx] 
             weight = len(Tj) / len(X[:, i])
             info_s += weight*Info(Tj)
         gain.append(info - info_s)

        else:  # непрерывный признак
            # сортируем столбец по возрастанию
            val = np.sort(X[:, i])

            local_gain = np.zeros(m - 1)

            # количество порогов на 1 меньше числа примеров
            for j in range(m - 1):
                threshold = val[j]
                less = sum(X[:, i] <= threshold)  # количество значений в столбце, <=, чем порог
                greater = m - less  # количество значений в столбце, >, чем порог

                # вычисляем информативность признака при данном пороге
                info_s = (less / m) * Info(Y[X[:, i] <= threshold]) + (greater / m) * Info(Y[X[:, i] > threshold])

                local_gain[j] = info - info_s

            gain.append(np.max(local_gain, axis=0))
            idx = np.argmax(local_gain, axis=0)

            thresholds[i] = val[idx]

    # теперь нужно выбрать столбец с максимальным приростом информации
    max_idx = np.argmax(gain)

    if scale[max_idx] == CATEGORICAL:
        # если этот столбец категориальный
        # запускаем цикл по всем уникальным значениям этого столбца
        categories = np.unique(X[:, max_idx])

        for category in categories:
            
            sub_x = X[X[:, max_idx] == category, :]
            sub_y = Y[X[:, max_idx] == category]

            print_indent(level)
            print('column %d == %f, ' % (max_idx, category), end='')

            decision_tree(sub_x, sub_y, scale, level + 1)
    else:
       
        threshold = thresholds[max_idx]

        sub_x = X[X[:, max_idx] <= threshold, :]
        sub_y = Y[X[:, max_idx] <= threshold]

        print_indent(level)
        print('column %d <= %f, ' % (max_idx, threshold), end='')

        decision_tree(sub_x, sub_y, scale, level + 1)

        sub_x = X[X[:, max_idx] > threshold, :]
        sub_y = Y[X[:, max_idx] > threshold]

        print_indent(level)
        print('column %d >  %f, ' % (max_idx, threshold), end='')

        decision_tree(sub_x, sub_y, scale, level + 1)
        
# вычисление энтропии множества set
def Info(set):
    m = len(set)
    info = 0
    
    n = np.unique(set)
    for i in n:
        p = np.sum(set == i) / m
        info += p * np.log2(p) if p > 0 else 0
    return -info

def print_indent(level):
    print(level * '  ', end='')
