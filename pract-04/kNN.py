import numpy as np
import math

def k_nearest(X, k, obj):
    # TODO: выполнить нормализацию каждого столбца (кроме последнего)
    sub_X = X[:, 0:-1]
    mx=np.max(sub_X, axis=0)
    norm_X = sub_X/mx
    # TODO: зная параметры среднего и среднеквадратического отклонения  по каждому столбцу sub_X, выполнить нормализацию объекта obj
    norm_obj = obj/mx
    
    # TODO: рассчитать евклидово расстояние от obj до каждого объекта sub_X 
    distance = np.zeros((16, k-1))
    for i in range(16):
       distance[i] = dist(norm_X[i], norm_obj)
   
    # TODO: Получить с помощью функции np.argsort индексы соседей по мере их удаления от obj.
    ind = np.argsort(distance, axis=0)
    
    # TODO: выбрать в отдельный вектор классы k ближайших соседей
    nearest_classes = np.zeros((4))
    for i in range(4):
        index = ind[i,0]
        nearest_classes[i] = X[[index], -1]   

    # TODO: определить наиболее часто встречающийся класс в этом векторе. 
    unique, counts = np.unique(nearest_classes, return_counts=True)
    object_class = unique[np.argmax(counts)]
    # TODO: вернуть полученное значение из функции. Искомый класс объекта obj хранится в переменной object_class
    return object_class

# вычисление евклидова расстояния между двумя точками
def dist(p1, p2):
    return math.sqrt(sum((p1-p2)**2))
