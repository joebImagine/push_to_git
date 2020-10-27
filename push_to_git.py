
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
        # If needed, creates the base folders where data is stored
        self.create_base_folders()

        # Inits the ui
        self.initUI()

    def initUI(self):
        # Initialize main layout and add children
        self.grid = QGridLayout()
        self.grid.addLayout(self.stored_location_layout(), 0, 0, 1, 4)
        self.grid.addWidget(self.push_to_group_layout(), 1, 0, 1, 4)

        # Set the stretch of the rows
        self.grid.setRowStretch(1, 1)
        self.grid.setRowStretch(2, 1)
        self.grid.setContentsMargins(32, 32, 32, 32)
        self.setLayout(self.grid)


class MainWindow(QMainWindow):
    def __init__(self, widget):
        QMainWindow.__init__(self)
        self.setWindowTitle("Push to git")

        # Init the Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit action
        exit_action = QAction(" Exit", self)
        exit_action.setShortcut("Ctrl+W")
        exit_action.triggered.connect(widget.exit_app)
        # Add repo action
        open_dir = QAction("Add Repo Location", self)
        open_dir.setShortcut("Ctrl+O")
        open_dir.triggered.connect(widget.add_repo_dialog)

        self.file_menu.addAction(open_dir)
        self.file_menu.addAction(exit_action)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Set the app style.

    widget = Widget()
    window = MainWindow(widget)
    window.setFixedSize(700, 400)
    window.show()

    sys.exit(app.exec_())
