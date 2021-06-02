import numpy as np
import matplotlib.pyplot as plt
import random

from sklearn import linear_model
from PIL import Image, ImageDraw 

#открытие изображения
im = Image.open('D:\Учёба Курс 2 Семестр 2\Python\Python Pract\Pract-06\Pract-06 v.1\image.jpg')
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

#построение кривой, описывающая оттенки строки изображения
lm = linear_model.LinearRegression()
lm.fit(X, y1) #blue
predicted = lm.predict(X)
plt.plot(x, y1, 'grey') #реальные значения
plt.plot(predicted, 'b') #предсказанные
plt.title('Описание строки изобржения с помощью полинома 5 степени (blue)')
plt.grid()
plt.show()

lm = linear_model.LinearRegression()
lm.fit(X, y2) #green
predicted = lm.predict(X)
plt.plot(x, y2, 'grey') #реальные значения
plt.plot(predicted, 'b') #предсказанные
plt.title('Описание строки изобржения с помощью полинома 5 степени (green)')
plt.grid()
plt.show()

lm = linear_model.LinearRegression()
lm.fit(X, y3) #red
predicted = lm.predict(X)
plt.plot(x, y3, 'grey') #реальные значения
plt.plot(predicted, 'b') #предсказанные
plt.title('Описание строки изобржения с помощью полинома 5 степени (red)')
plt.grid()
plt.show()

#кодирование разностей
raz=y1 -predicted#разность
bits_per_channel = 4#задаем сколько бит потребуется для хранения разностей в каждой точке
threshold=bits_per_channel*2
diff=np.clip(raz)
y = predicted + diff

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
del draw

#Привести результаты кодирования изображения 3, 4, 5, 6 и 7 битами, а также исходное изображение. 
raz=y1 -predicted#разность
bits_per_channel = 3 
threshold=bits_per_channel*2
diff=np.clip(raz)
y = predicted + diff 
raz=y1 -predicted#разность
bits_per_channel = 5 
threshold=bits_per_channel*2
diff=np.clip(raz)
y = predicted + diff 
raz=y1 -predicted#разность
bits_per_channel = 6 
threshold=bits_per_channel*2
diff=np.clip(raz)
y = predicted + diff 
raz=y1 -predicted#разность
bits_per_channel = 7 
threshold=bits_per_channel*2
diff=np.clip(raz)
y = predicted + diff 