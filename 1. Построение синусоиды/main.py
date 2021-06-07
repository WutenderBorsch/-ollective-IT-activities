from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog

import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, uic

import sys

class Window(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('View.ui', self)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.verticalLayout.insertWidget(0, self.canvas)
        self.ax = self.figure.add_subplot(111)
        x = np.arange(-5 * np.pi, 5 * np.pi, 0.1)
        y = np.cos(x)
        self.ax.plot(x, y, '-')
        self.horizontalSlider.valueChanged.connect(self.widthChanged)
        self.canvas.draw()

    def widthChanged(self):
        newValue = self.horizontalSlider.value()
        self.ax.clear()
        x = np.arange(-newValue * np.pi, newValue * np.pi, 0.1)
        y = np.cos(x)
        self.ax.plot(x, y, '-')
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())