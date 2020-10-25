from PySide2.QtCore import Qt, Slot
from PySide2.QtWidgets import (
    QApplication, QWidget, QFileDialog
)
from pathlib import Path
from my_utils import Utils
import constants

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
    def add_repo_dialog(self):
        utils = Utils()
        home_dir = str(Path.home())
        curr_dir = QFileDialog.getExistingDirectory(self, 'Open File', home_dir, QFileDialog.ShowDirsOnly)

        if curr_dir:
            utils.set_list_item(constants.repo_location_storage_path, curr_dir)
            # add the item to the drop-down
            self.stored_dir_dropdown.addItem(curr_dir)
            self.stored_dir_dropdown.setCurrentText(curr_dir)

    @Slot()
    def get_list_items(self):
        utils = Utils()
        folder_path = constants.repo_location_storage_path
        full_path = f"{folder_path}/{constants.list_items_file_name}"

        # Check if the file exists.  If it doesn't, create it
        utils.create_file(full_path)
        arr = []
        # get all of the items from the file and convert to a list
        with open(full_path) as my_file:
            for line in my_file:
                arr.append(str.rstrip(line))

        return arr
