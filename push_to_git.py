
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
        self.file_title = QLabel('File Location:')
        self.file_location_edit = QLineEdit()
        self.file_location_edit.setStyleSheet("background: #2C2B2B;")
        self.open_file_btn = QPushButton("Open")

        UI_Layout = Layout()

        # Initialize main layout and add children
        self.grid = QGridLayout()
        self.grid.addWidget(self.file_title, 0, 0)
        self.grid.addWidget(self.file_location_edit, 0, 1)
        self.grid.addWidget(self.open_file_btn, 0, 2)
        self.grid.addLayout(UI_Layout.stored_location_layout(), 1, 0, 1, 3)
        # self.grid.addWidget(self.storedDirDropDown, 1, 1)
        self.grid.addWidget(UI_Layout.push_to_group_layout(), 2, 0, 1, 3)
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
