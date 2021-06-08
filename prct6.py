import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model
from PIL import Image, ImageDraw

# открытие изображения
im = Image.open(r'C:\Users\anast\Desktop\image.png')
data = np.array(im.getdata()).reshape([im.height, im.width, 3])

# создание матрицы входных признаков
x = np.arange(0, im.width)
X = np.array([x, x ** 2.0, x ** 3.0, x ** 4.0, x ** 5.0]).transpose()

# построение и визуализация полинома
y1 = data[0, :, 2]  # оттенки у хранятся в массиве data. Трехмерный массив.
# 1 инд описывает строку изображения, 2ой - столбец изображения, 3ий - цветовой канал(RGB).
y2 = data[0, :, 1]
y3 = data[0, :, 0]
plt.plot(x, y1, 'b')
plt.plot(x, y2, 'g')
plt.plot(x, y3, 'r')
plt.title('Цветовые каналы первой строки изображения')
plt.grid()
plt.show()


# построение кривой, описывающей оттенки строки изображения
def plottingСurve(y):
    lm = linear_model.LinearRegression()
    lm.fit(X, y)
    predicted = lm.predict(X)
    #plt.plot(x, y, 'grey')  # реальные значения
    #plt.plot(predicted, 'b')  # предсказанные
    #plt.title('Описание строки изобржения с помощью полинома 5 степени')
    #plt.grid()
    #plt.show()
    return predicted


# кодирование разностей
def differences(c_y, i):
    c_predicted = plottingСurve(c_y)
    raz = c_y - c_predicted  # разность
    threshold = i * 2
    diff = np.clip(raz, threshold, -threshold)
    y = c_predicted + diff
    return y


# подмена пикселов в исходном изображении
draw = ImageDraw.Draw(im)  # создаем инструмент для рисования.
width = im.size[0]  # определяем ширину.
height = im.size[1]  # определяем высоту.

bit = [3, 4, 5, 6, 7]

B = []
G = []
R = []

for i in range(len(bit)):
    B.append(differences(y1, bit[i]))
    G.append(differences(y2, bit[i]))
    R.append(differences(y3, bit[i]))
    
im.save('C:\\Users\\anast\Desktop\image1.png')

# Привести результаты кодирования изображения 3, 4, 5, 6 и 7 битами, а также исходное изображение.

for b in range(len(bit)):
    for i in range(width):
        for j in range(height):
            cr = int(R[b][i])
            cg = int(G[b][i])
            cb = int(B[b][i])
            S = (cr + cg + cb) // 3
            draw.point((i, j), (S, S, S))
    im.save('C:\\Users\\anast\Desktop\\' + str(b) + '.png')

del draw