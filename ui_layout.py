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
    def __init__(self):
        super().__init__()

    def stored_location_layout(self):
        self.stored_directories_title = QLabel(constants.stored_dir_str)

        # Combo box and its properties
        self.stored_dir_dropdown = QComboBox()
        self.stored_dir_dropdown.addItems(self.get_list_items())
        self.stored_dir_dropdown.setCursor(QCursor(Qt.PointingHandCursor))
        self.stored_dir_dropdown.setStyleSheet(stored_dir_dropdown_styles)

        # Layout grid for combo box widget
        self.stored_dirs_layout = QGridLayout()
        self.stored_dirs_layout.addWidget(self.stored_directories_title, 0, 0)
        self.stored_dirs_layout.addWidget(self.stored_dir_dropdown, 0, 1)
        self.stored_dirs_layout.setColumnStretch(1, 2)
        self.stored_dirs_layout.setContentsMargins(0, 16, 0, 32)

        return self.stored_dirs_layout

    def push_to_group_layout(self):
        # Create a group
        self.group_push_to = QGroupBox(constants.push_branch_str)
        self.group_push_to.setStyleSheet(group_widgets_styles)

        # Create the layout for the branch widgets
        self.pushToLayout = QVBoxLayout()
        self.pushToLayout.setAlignment(Qt.AlignTop)
        self.pushToLayout.setContentsMargins(16, 24, 16, 24)

        # Set the layout to the group
        self.group_push_to.setLayout(self.pushToLayout)

        # Create the staging button and its properties
        self.staging_btn = QPushButton(constants.master_to_staging_str)
        self.staging_btn.clicked.connect(
            lambda: self.handle_branch_push_to_git(
                constants.master, constants.staging
            )
        )
        self.staging_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.staging_btn.setStyleSheet(button_styles)

        # Create the production button and its properties
        self.prod_btn = QPushButton(constants.staging_to_prod_str)
        self.prod_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.prod_btn.clicked.connect(
            lambda: self.handle_branch_push_to_git(
                constants.staging, constants.production
            )
        )
        self.prod_btn.setStyleSheet(button_styles)

        # Add the button widgets to the layout
        self.pushToLayout.addWidget(self.staging_btn)
        self.pushToLayout.addWidget(self.prod_btn)

        return self.group_push_to
