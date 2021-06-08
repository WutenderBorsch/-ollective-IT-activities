import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.x = 0
        patch = QFileDialog.getExistingDirectory(None, "Select folder", ".")

        if patch == '':
            quit()

        files = os.listdir(patch)

        self.images = []

        for x in files:
            if x.endswith('.png'):
                self.images.append(patch + "\\" + x)

        if len(self.images) == 0:
            quit()

        self.label = QLabel(self)

        pixmap = QPixmap(str(self.images[0]))

        self.label.setPixmap(pixmap)
        self.label.setMaximumWidth(500)
        self.label.setMaximumHeight(500)

        self.left = QPushButton("<--")
        self.fight = QPushButton("-->")

        self.x = 0

        self.left.clicked.connect(lambda: self.Left())
        self.fight.clicked.connect(lambda: self.Right())

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.grid.addWidget(self.left, 3, 0)
        self.grid.addWidget(self.fight, 3, 1)

        self.grid.addWidget(self.label, 0, 0, 0, 2)


    def Left(self):
        if self.x == 0:
            return

        self.x -= 1

        pixmap = QPixmap(str(self.images[self.x]))
        return self.label.setPixmap(pixmap)

    def Right(self):
        if self.x == len(self.images) - 1:
            return

        self.x += 1
        pixmap = QPixmap(str(self.images[self.x]))
        return self.label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())

