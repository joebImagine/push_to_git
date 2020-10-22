from PySide2.QtCore import Qt, Slot
from PySide2.QtWidgets import (
    QApplication, QLabel, QMainWindow, QTableWidget, QVBoxLayout,
    QWidget, QGridLayout, QPushButton, QGroupBox, QComboBox, QLineEdit
)
from PySide2.QtGui import QCursor
from stylesheet import stored_dir_dropdown_styles, group_widgets_styles, button_styles


class Layout(QWidget):

    def stored_location_layout(self):
        self.stored_directories_title = QLabel("Pick a stored location: ")
        self.stored_dir_dropdown = QComboBox()
        self.stored_dir_dropdown.setCursor(QCursor(Qt.PointingHandCursor))
        self.stored_dir_dropdown.setStyleSheet(stored_dir_dropdown_styles)
        self.stored_dirs_layout = QGridLayout()
        self.stored_dirs_layout.addWidget(self.stored_directories_title, 0, 0)
        self.stored_dirs_layout.addWidget(self.stored_dir_dropdown, 0, 1)
        self.stored_dirs_layout.setColumnStretch(1, 2)
        self.stored_dirs_layout.setContentsMargins(0, 16, 0, 32)

        return self.stored_dirs_layout

    def push_to_group_layout(self):
        self.group_push_to = QGroupBox("Push to: ")
        self.group_push_to.setStyleSheet(group_widgets_styles)
        self.vBox1 = QVBoxLayout()
        # self.vBox1.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.vBox1.setAlignment(Qt.AlignTop)
        self.vBox1.setContentsMargins(16, 24, 16, 24)
        self.group_push_to.setLayout(self.vBox1)
        self.staging_btn = QPushButton("Staging")
        self.prod_btn = QPushButton("Production")
        self.staging_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.prod_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.staging_btn.setStyleSheet(button_styles)
        self.prod_btn.setStyleSheet(button_styles)
        # self.staging_btn.setFixedSize(150, 40)
        # self.prod_btn.setFixedSize(150, 40)
        self.vBox1.addWidget(self.staging_btn)
        self.vBox1.addWidget(self.prod_btn)

        return self.group_push_to

    def file_location_layout(self):
        self.file_title = QLabel('Repo Location:')
        self.file_location_edit = QLineEdit()
        self.file_location_edit.setStyleSheet("background: #2C2B2B;")
        self.open_file_btn = QPushButton("Open")
        self.store_btn = QPushButton("Store")
        self.open_file_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.store_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.file_location_layout = QGridLayout()
        self.file_location_layout.setColumnStretch(1, 2)

        self.file_location_layout.addWidget(self.file_title, 0, 0, 1, 1)
        self.file_location_layout.addWidget(
            self.file_location_edit, 0, 1, 1, 2)
        self.file_location_layout.addWidget(self.open_file_btn, 0, 3, 1, 1)
        self.file_location_layout.addWidget(self.store_btn, 0, 4, 1, 1)

        return self.file_location_layout

    def fetch_origin_layout(self):
        self.group_fetch_origin = QGroupBox("Fetch origin: ")
        self.group_fetch_origin.setStyleSheet(group_widgets_styles)
        self.grid1 = QGridLayout()
        self.master_btn = QPushButton("Master")
        self.main_btn = QPushButton("Main")
        self.staging_btn = QPushButton("Staging")
        self.prod_btn = QPushButton("Prod")
        self.master_btn.setStyleSheet(button_styles)
        self.main_btn.setStyleSheet(button_styles)
        self.staging_btn.setStyleSheet(button_styles)
        self.prod_btn.setStyleSheet(button_styles)
        self.main_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.master_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.staging_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.prod_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.grid1.setContentsMargins(16, 24, 16, 24)
        self.grid1.addWidget(self.master_btn, 0, 0)
        self.grid1.addWidget(self.main_btn, 0, 1)
        self.grid1.addWidget(self.staging_btn, 1, 0, 1, 2)
        self.grid1.addWidget(self.prod_btn, 2, 0, 1, 2)
        self.grid1.setAlignment(Qt.AlignTop)
        self.group_fetch_origin.setLayout(self.grid1)

        return self.group_fetch_origin
