import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
w = QWidget()

patch = QFileDialog.getExistingDirectory(None, "Select folder", ".")

if patch == '':
    quit()

files = os.listdir(patch)

images = []

for x in files:
    if x.endswith('.png'):
        images.append(patch + "\\" + x)

if len(images) == 0:
    quit()

lable = QLabel(w)

pixmap = QPixmap(str(images[0]))

lable.setPixmap(pixmap)
lable.setMaximumWidth(500)
lable.setMaximumHeight(500)


class Container:
    def __init__(self, x):
        self.x = x

def Left(i):
    if i.x == 0:
        return

    i.x -= 1

    pixmap = QPixmap(str(images[i.x]))
    lable.setPixmap(pixmap)
    return

def Right(i):
    if i.x == len(images) - 1:
        return

    i.x += 1
    pixmap = QPixmap(str(images[i.x]))
    lable.setPixmap(pixmap)
    return

def main():

    left = QPushButton("<--")
    fight = QPushButton("-->")

    x = Container(0)

    left.clicked.connect(lambda: Left(x))
    fight.clicked.connect(lambda: Right(x))

    grid = QGridLayout();
    w.setLayout(grid)

    grid.addWidget(lable, 0, 0, 0, 2)

    grid.addWidget(left, 3, 0)
    grid.addWidget(fight, 3, 1)

    w.show()


main()
sys.exit(app.exec_())