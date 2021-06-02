import numpy as np
import math

def k_nearest(X, k, obj):
    
    # нормализация каждого столбца (кроме последнего)
    mx=np.max(X[:, 0:-1], axis=0)
    norm_X = X[:, 0:-1]/mx
    
    # нормализация объекта obj
    norm_obj = obj/mx
    distance = np.zeros((len(X), k-1))
    for i in range(len(X)):
       distance[i] = dist(norm_X[i], norm_obj)
    # получение с помощью функции np.argsort индексы соседей по мере их удаления от obj.
    sort = np.argsort(distance, axis=0)
    
    # выборка в отдельный вектор классы k ближайших соседей
    nearest_classes = np.zeros((4))
    for i in range(4):
        index = sort[i,0]
        nearest_classes[i] = X[[index], -1]   

    # наиболее часто встречающийся класс в этом векторе
    unique, counts = np.unique(nearest_classes, return_counts=True)
    object_class = unique[np.argmax(counts)]
    return object_class

# вычисление евклидова расстояния между двумя точками
def dist(p1, p2):
    return math.sqrt(sum((p1-p2)**2))

