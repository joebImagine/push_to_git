
#!/usr/local/opt/python@3.8/bin/python3.8
import sys
from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QPainter, QColor, QPalette
from PySide2.QtWidgets import (
    QApplication, QLabel, QMainWindow, QWidget, QGridLayout,
    QLineEdit, QPushButton, QHBoxLayout, QComboBox
)
from my_utils import Color
from ui_layout import Layout


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.fileTitle = QLabel('File Location:')
        self.fileLocationEdit = QLineEdit()
        self.fileLocationEdit.setStyleSheet("background: #2C2B2B;")
        self.openFileBtn = QPushButton("Open")

        UILayout = Layout()

        # Initialize main layout and add children
        self.grid = QGridLayout()
        self.grid.addWidget(self.fileTitle, 0, 0)
        self.grid.addWidget(self.fileLocationEdit, 0, 1)
        self.grid.addWidget(self.openFileBtn, 0, 2)
        self.grid.addLayout(UILayout.storedLocationLayout(), 1, 0, 1, 3)
        # self.grid.addWidget(self.storedDirDropDown, 1, 1)
        self.grid.addWidget(UILayout.pushToGroupLayout(), 2, 0, 1, 3)
        # Set the stretch of the rows
        self.grid.setRowStretch(1, 1)
        self.grid.setRowStretch(2, 1)
        # self.grid.setVerticalSpacing(48)
        self.grid.setContentsMargins(32, 32, 32, 32)
        # self.grid.addWidget(Color('red'))
        self.setLayout(self.grid)



class MainWindow(QMainWindow):
    def __init__(self, widget):
        QMainWindow.__init__(self)
        self.setWindowTitle("Push to git")
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion') # Set the app style.

    widget = Widget()
    window = MainWindow(widget)
    window.setFixedSize(500, 600)
    window.show()

    sys.exit(app.exec_())
