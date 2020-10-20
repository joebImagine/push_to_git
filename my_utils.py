import sys
from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QPainter, QColor, QPalette
from PySide2.QtWidgets import (
    QAction, QApplication, QLabel, QSpinBox,
    QMainWindow, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget, QGridLayout, QDoubleSpinBox
)
from PySide2.QtCharts import QtCharts

class Color(QWidget):

    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
