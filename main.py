import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QGraphicsScene, QGraphicsView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
import random


class CircleInterface(QWidget):
    def __init__(self):
        super(CircleInterface, self).__init__()

        self.button = QPushButton('Создать', self)
        self.button.clicked.connect(self.create_random_circle)

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)
        self.view.setAlignment(Qt.AlignTop)

        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(self.button)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


