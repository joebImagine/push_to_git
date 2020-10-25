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
    def add_repo_dialog(self):
        # Import the Utils class
        utils = Utils()
        # Set the home directory path
        home_dir = str(Path.home())
        # Set the retrieved curr directory path
        curr_dir = QFileDialog.getExistingDirectory(self, 'Open File', home_dir, QFileDialog.ShowDirsOnly)

        # Check if the curr_dir has a value.  If so, store that directory to the file
        if curr_dir:
            utils.set_list_item(constants.repo_location_storage_path, curr_dir)
            # add the item to the drop-down
            self.stored_dir_dropdown.addItem(curr_dir)
            self.stored_dir_dropdown.setCurrentText(curr_dir)

    @Slot()
    def get_list_items(self):
        # Import the Utils class
        utils = Utils()
        # Set the folder path
        folder_path = constants.repo_location_storage_path
        # Set the path including the file name
        full_path = f"{folder_path}/{constants.list_items_file_name}"

        # Check if the file exists.  If it doesn't, create it
        utils.create_file(full_path)
        arr = []
        # Get all of the items from the file and convert to a list
        with open(full_path) as my_file:
            for line in my_file:
                arr.append(str.rstrip(line))

        return arr
