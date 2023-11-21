import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGraphicsView, QGraphicsScene, QVBoxLayout, QWidget \
    , QGraphicsEllipseItem
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

        self.setLayout(layout)

    def create_random_circle(self):
        diameter = random.randint(20, 100)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        circle = QGraphicsEllipseItem(0, 0, diameter, diameter)
        circle.setBrush(color)
        self.scene.addItem(circle)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.interface = CircleInterface()
        self.setCentralWidget(self.interface)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
