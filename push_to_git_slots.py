import os
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
        self.home_dir = str(Path.home())
        self.utils = Utils()

    @Slot()
    def exit_app(self, checked):
        QApplication.quit()

    @Slot()
    def add_repo_dialog(self):
        # Set the home directory path
        # Set the retrieved curr directory path
        curr_dir = QFileDialog.getExistingDirectory(self, 'Open File', self.home_dir, QFileDialog.ShowDirsOnly)

        # Check if the curr_dir has a value.  If so, store that directory to the file
        if curr_dir:
            self.utils.set_list_item(f"{self.home_dir}{constants.repo_location_storage_path}", curr_dir)
            # add the item to the drop-down
            self.stored_dir_dropdown.addItem(curr_dir)
            self.stored_dir_dropdown.setCurrentText(curr_dir)

    @Slot()
    def create_base_folders(self):
        # Create the base dir
        self.utils.create_dir(f"{self.home_dir}/push_to_git_storage")
        # Set the folder path
        folder_path = f"{self.home_dir}{constants.repo_location_storage_path}"
        # Create the storage dir
        self.utils.create_dir(folder_path)


    @Slot()
    def get_list_items(self):
        # Set the path including the file name
        full_path = f"{self.home_dir}{constants.repo_location_storage_path}/{constants.list_items_file_name}"

        # Check if the file exists.  If it doesn't, create it
        self.utils.create_file(full_path)
        arr = []
        # Get all of the items from the file and convert to a list
        with open(full_path) as my_file:
            for line in my_file:
                arr.append(str.rstrip(line))

        return arr

    @Slot()
    def set_branch_item(self, prefix):
        # Get the current repo directory path. Then parse the data to retrieve only the
        # directory name
        curr_repo_name = self.stored_dir_dropdown.currentText()
        curr_repo_name = curr_repo_name.rsplit('/', 1)[1]

        # Set the folders path
        dates_storage_path = f"{self.home_dir}{constants.dates_time_storage_path}"
        curr_repo_folder_path = f"{dates_storage_path}/{curr_repo_name}"
        prefix_folder_path =  f"{curr_repo_folder_path}/{prefix}"

        # Set the file name which is the prefix with the current formatted date
        prefix_with_curr_date = f"{prefix}_{self.utils.current_formatted_date()}.txt"

        # Full path for file name
        full_path_to_prefix_file = f"{prefix_folder_path}/{prefix_with_curr_date}"

        folder_paths = [
            dates_storage_path,
            curr_repo_folder_path,
            prefix_folder_path
        ]

        # Generate the directories
        for key in folder_paths:
            self.utils.create_dir(key)

        # Create the storage file and check what the version number should be
        dates_storage_file = self.utils.create_or_read_file(full_path_to_prefix_file)
        lines = dates_storage_file.readlines()
        version_num = len(lines) + 1
        dates_storage_file.close()

        # Create the branch
        self.branch_name = f'{prefix}_{self.utils.current_formatted_date()}v{version_num}'

        dates_storage_file = open(full_path_to_prefix_file, 'a+')
        dates_storage_file.write(f'{self.branch_name}\n')

        dates_storage_file.close()
