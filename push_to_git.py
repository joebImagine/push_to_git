
import sys
from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QPainter, QColor, QPalette
from PySide2.QtWidgets import (
    QAction, QApplication, QLabel, QSpinBox,
    QMainWindow, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget, QGridLayout, QDoubleSpinBox
)
from PySide2.QtCharts import QtCharts


class Widget(QWidget):
    def __init__(self):
        super().__init__()

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Push to git")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.resize(600, 400)
    window.show()

    sys.exit(app.exec_())
