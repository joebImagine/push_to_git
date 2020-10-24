from PySide2.QtCore import Qt, Slot
from PySide2.QtWidgets import (
    QApplication, QWidget, QFileDialog
)
from pathlib import Path


class Slots(QWidget):
    def __init__(self):
        super().__init__()

    @Slot()
    def exit_app(self, checked):
        QApplication.quit()

    @Slot()
    def get_selected_repo_location(self):
        print(self.stored_dir_dropdown.currentText())

    @Slot()
    def show_dialog(self):
        home_dir = str(Path.home())
        curr_dir = QFileDialog.getExistingDirectory(self, 'Add Repo', home_dir)
        print(curr_dir)
