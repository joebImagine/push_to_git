from PySide2.QtCore import Qt, Slot
from PySide2.QtWidgets import (
    QApplication, QLabel, QMainWindow, QTableWidget, QVBoxLayout,
    QWidget, QGridLayout, QPushButton, QGroupBox, QComboBox, QLineEdit
)
from PySide2.QtGui import QCursor
from stylesheet import stored_dir_dropdown_styles, group_widgets_styles, button_styles
from push_to_git_slots import Slots
import constants


class Layout(Slots):
    def stored_location_layout(self):
        self.stored_directories_title = QLabel(constants.stored_dir_str)
        self.stored_dir_dropdown = QComboBox()
        self.stored_dir_dropdown.addItems(self.get_list_items())
        self.stored_dir_dropdown.setCursor(QCursor(Qt.PointingHandCursor))
        self.stored_dir_dropdown.setStyleSheet(stored_dir_dropdown_styles)
        self.stored_dirs_layout = QGridLayout()
        self.stored_dirs_layout.addWidget(self.stored_directories_title, 0, 0)
        self.stored_dirs_layout.addWidget(self.stored_dir_dropdown, 0, 1)
        self.stored_dirs_layout.setColumnStretch(1, 2)
        self.stored_dirs_layout.setContentsMargins(0, 16, 0, 32)

        return self.stored_dirs_layout

    def push_to_group_layout(self):
        self.group_push_to = QGroupBox("Push branch: ")
        self.group_push_to.setStyleSheet(group_widgets_styles)
        self.vBox1 = QVBoxLayout()
        self.vBox1.setAlignment(Qt.AlignTop)
        self.vBox1.setContentsMargins(16, 24, 16, 24)
        self.group_push_to.setLayout(self.vBox1)

        # Create the staging button and its properties
        self.staging_btn = QPushButton(constants.master_to_staging_str)
        self.staging_btn.clicked.connect(
            lambda: self.handle_branch_push_to_git("master", "staging"))
        self.staging_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.staging_btn.setStyleSheet(button_styles)

        # Create the production button and its properties
        self.prod_btn = QPushButton(constants.staging_to_prod_str)
        self.prod_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.prod_btn.clicked.connect(
            lambda: self.handle_branch_push_to_git("staging", "production"))

        self.prod_btn.setStyleSheet(button_styles)

        self.vBox1.addWidget(self.staging_btn)
        self.vBox1.addWidget(self.prod_btn)

        return self.group_push_to
