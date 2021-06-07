import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model
from PIL import Image, ImageDraw 

#открытие изображения
im = Image.open(r'D:\Учёба Курс 2 Семестр 2\Python\Python Pract\Pract-06\Pract-06 v.1\image.jpg')
data = np.array(im.getdata()).reshape([im.height, im.width,3])

#создание матрицы входных признаков
x = np.arange(0, im.width)
X = np.array([x, x**2.0, x**3.0, x**4.0, x**5.0]).transpose()
    
#построение и визуализация полинома
y1 = data[0, :, 2] #оттенки у хранятся в массиве data. Трехмерный массив.
#1 инд описывает строку изображения, 2ой - столбец изображения, 3ий - цветовой канал(RGB).
y2 = data[0, :, 1]
y3 = data[0, :, 0]
plt.plot(x, y1, 'b')
plt.plot(x, y2, 'g')
plt.plot(x, y3, 'r')
plt.title('Цветовые каналы первой строки изображения')
plt.grid()
plt.show()

#построение кривой, описывающей оттенки строки изображения
def function(y):
	lm = linear_model.LinearRegression()
	lm.fit(X, y)
	predicted = lm.predict(X)
	plt.plot(x, y, 'grey') #реальные значения
	plt.plot(predicted, 'b') #предсказанные
	plt.title('Описание строки изобржения с помощью полинома 5 степени')
	plt.grid()
	plt.show()
	return predicted

#кодирование разностей
def differences(c_y, i):
    c_predicted = function(c_y)
    raz = c_y - c_predicted #разность
    bits_per_channel = i #задаем сколько бит потребуется для хранения разностей в каждой точке
    threshold=bits_per_channel*2
    diff=np.clip(raz, threshold, -threshold)
    y = c_predicted + diff
    return y

bit = [3, 4, 5, 6, 7]
B = []
G = []
R = []

for i in range(len(bit)):
    b_y = differences(y1, bit[i])
    g_y = differences(y2, bit[i])
    r_y = differences(y3, bit[i])
    B.append([])
    G.append([])
    R.append([])
    for j in range(1):
        B[i].append(b_y)
        G[i].append(g_y)
        R[i].append(r_y)
        

#подмена пикселов в исходном изображении
draw = ImageDraw.Draw(im) #создаем инструмент для рисования. 
width = im.size[0] #определяем ширину. 
height = im.size[1] #определяем высоту. 	
pix = im.load() #выгружаем значения пикселей.
for i in range(width):
	for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = (a + b + c) // 3
			draw.point((i, j), (S, S, S))
im.save('ready.png')

#Привести результаты кодирования изображения 3, 4, 5, 6 и 7 битами, а также исходное изображение. 	
for b in range(len(bit)):
    for i in range(width):
        for j in range(height):
            cr = int(R[b][0][i])
            cg = int(G[b][0][i])
            cb = int(B[b][0][i])
            S = (cr + cg + cb) // 3
            draw.point((i, j), (S, S, S))
    im.save(str(b) + '.png')
del draw
