
#!/usr/local/opt/python@3.8/bin/python3.8
import sys
from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QPainter, QColor, QPalette
from PySide2.QtWidgets import (
    QApplication, QLabel, QMainWindow, QWidget, QGridLayout,
    QLineEdit, QPushButton, QHBoxLayout, QComboBox, QAction, QFileDialog
)
from my_utils import Color
from ui_layout import Layout
from pathlib import Path


class Widget(Layout):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # Initialize main layout and add children
        self.grid = QGridLayout()
        self.grid.addLayout(self.file_location_layout(), 0, 0, 1, 4)
        self.grid.addLayout(self.stored_location_layout(), 1, 0, 1, 4)
        # self.grid.addWidget(self.stored_dir_dropdown, 1, 1)
        self.grid.addWidget(self.push_to_group_layout(), 2, 2, 1, 2)
        self.grid.addWidget(self.fetch_origin_layout(), 2, 0, 1, 2)
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

        # Init the Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit QAction
        exit_action = QAction(" Exit", self)
        open_file = QAction("Open", self)
        exit_action.setShortcut("Ctrl+W")
        open_file.setShortcut("Ctrl+O")
        open_file.triggered.connect(self.showDialog)
        exit_action.triggered.connect(self.exit_app)

        self.file_menu.addAction(open_file)
        self.file_menu.addAction(exit_action)
        self.setCentralWidget(widget)

    @Slot()
    def exit_app(self, checked):
        QApplication.quit()

    @Slot()
    def showDialog(self):

        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Set the app style.

    widget = Widget()
    window = MainWindow(widget)
    window.setFixedSize(700, 500)
    window.show()

    sys.exit(app.exec_())
