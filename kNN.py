import numpy as np
import math

def k_nearest(X, k, obj):
    
    # стандартизаия каждого столбца (кроме последнего)
    
    mean = X[:, 0:-1].mean(axis = 0)
    std = X[:, 0:-1].std(axis = 0)
    norm_X = X[:, 0:-1] - mean/std
    
    # стандартизация объекта obj
    norm_obj = obj - mean / std
    distance = [[dist(norm_X[i], norm_obj)] for i in range(len(X))]
    # получение с помощью функции np.argsort индексы соседей по мере их удаления от obj.
    sort = np.argsort(distance, axis=0)
    
    # выборка в отдельный вектор классы k ближайших соседей
    nearest_classes = [X[sort[i,0], -1] for i in range(k)]

    # наиболее часто встречающийся класс в этом векторе
    unique, counts = np.unique(nearest_classes, return_counts=True)
    object_class = unique[np.argmax(counts)]
    return object_class

# вычисление евклидова расстояния между двумя точками
def dist(p1, p2):
    return math.sqrt(sum((p1-p2)**2))


