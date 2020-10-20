from PySide2.QtCore import Qt, Slot
from PySide2.QtWidgets import (
    QApplication, QLabel, QMainWindow, QTableWidget, QVBoxLayout,
    QWidget, QGridLayout, QPushButton, QGroupBox, QComboBox
)
from stylesheet import storedDirDropDownStyles


class Layout(QWidget):

    def storedLocationLayout(self):

        self.storedDirectoriesTitle = QLabel("Pick a stored location: ")
        self.storedDirDropDown = QComboBox()
        self.storedDirDropDown.setStyleSheet(storedDirDropDownStyles)
        self.storedDirectoriesLayout = QGridLayout()
        self.storedDirectoriesLayout.addWidget(self.storedDirectoriesTitle, 0, 0)
        self.storedDirectoriesLayout.addWidget(self.storedDirDropDown, 0, 1)
        self.storedDirectoriesLayout.setColumnStretch(1, 2)
        self.storedDirectoriesLayout.setContentsMargins(0, 16, 0, 32)

        return self.storedDirectoriesLayout


    def pushToGroupLayout(self):

        self.groupWidgets = QGroupBox("Push to: ")
        self.groupWidgets.setStyleSheet(groupWidgetsStyles)
        self.vBox1 = QVBoxLayout()
        self.vBox1.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.vBox1.setContentsMargins(0, 24, 0, 24)
        self.groupWidgets.setLayout(self.vBox1)
        self.stagingBtn = QPushButton("Staging")
        self.prodBtn = QPushButton("Production")
        self.stagingBtn.setFixedSize(150, 40)
        self.prodBtn.setFixedSize(150, 40)
        self.vBox1.addWidget(self.stagingBtn)
        self.vBox1.addWidget(self.prodBtn)

        return self.groupWidgets
