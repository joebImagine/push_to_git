
import sys
from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QPainter, QColor, QPalette
from PySide2.QtWidgets import (
    QAction, QApplication, QLabel, QSpinBox,
    QMainWindow, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget, QGridLayout, QDoubleSpinBox,
    QTextEdit, QLineEdit, QPushButton, QGroupBox, QHBoxLayout,
    QComboBox
)
from PySide2.QtCharts import QtCharts

import my_utils

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.fileTitle = QLabel('File Location:')
        self.fileLocationEdit = QLineEdit()
        self.openFileBtn = QPushButton("Open")

        # Initialize main layout and add children
        self.grid = QGridLayout()
        self.grid.addWidget(self.fileTitle, 0, 0)
        self.grid.addWidget(self.fileLocationEdit, 0, 1)
        self.grid.addWidget(self.openFileBtn, 0, 2)
        self.grid.addLayout(self.storedLocationLayout(), 1, 0, 1, 4)
        # self.grid.addWidget(self.storedDirDropDown, 1, 1)
        self.grid.addWidget(self.pushToGroupLayout(), 2, 0, 1, 4)
        # Set the stretch of the rows
        self.grid.setRowStretch(1, 1)
        self.grid.setRowStretch(2, 1)
        # self.grid.setVerticalSpacing(48)
        self.grid.setContentsMargins(32, 32, 32, 32)
        # self.grid.addWidget(my_utils.Color('red'))
        self.setLayout(self.grid)

    def storedLocationLayout(self):
        self.storedDirectoriesTitle = QLabel("Pick a stored location: ")
        self.storedDirDropDown = QComboBox()
        self.storedDirectoriesLayout = QGridLayout()
        self.storedDirectoriesLayout.addWidget(self.storedDirectoriesTitle, 0, 0)
        self.storedDirectoriesLayout.addWidget(self.storedDirDropDown, 0, 1)
        self.storedDirectoriesLayout.setColumnStretch(1, 2)
        self.storedDirectoriesLayout.setContentsMargins(0, 16, 0, 32)

        return self.storedDirectoriesLayout

    def pushToGroupLayout(self):
        self.groupWidgets = QGroupBox("Push to: ")
        self.groupWidgets.setStyleSheet(
            "QGroupBox:title {font-size:14px; margin: 0;}"
        )
        self.vBox1 = QVBoxLayout()
        self.vBox1.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.groupWidgets.setLayout(self.vBox1)
        self.stagingBtn = QPushButton("Staging")
        self.prodBtn = QPushButton("Production")
        self.stagingBtn.setFixedSize(150, 40)
        self.prodBtn.setFixedSize(150, 40)
        self.vBox1.addWidget(self.stagingBtn)
        self.vBox1.addWidget(self.prodBtn)

        return self.groupWidgets



class MainWindow(QMainWindow):
    def __init__(self, widget):
        QMainWindow.__init__(self)
        self.setWindowTitle("Push to git")
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = Widget()
    window = MainWindow(widget)
    window.resize(600, 400)
    window.show()

    sys.exit(app.exec_())
