import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget


class CircleInterface(QWidget):
    def __init__(self):
        super(CircleInterface, self).__init__()

        self.button = QPushButton('Создать', self)
        self.button.clicked.connect(self.create_random_circle)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


