import os
import subprocess
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

    def exit_app(self, checked):
        QApplication.quit()

    def add_repo_dialog(self):
        # Set the home directory path
        # Set the retrieved curr directory path
        curr_dir = QFileDialog.getExistingDirectory(
            self, 'Open File', self.home_dir, QFileDialog.ShowDirsOnly)

        # Check if the curr_dir has a value.  If so, store that directory to the file
        if curr_dir:
            self.utils.set_list_item(
                f"{self.home_dir}{constants.repo_location_storage_path}", curr_dir)
            # add the item to the drop-down
            self.stored_dir_dropdown.addItem(curr_dir)
            self.stored_dir_dropdown.setCurrentText(curr_dir)

    def create_base_folders(self):
        # Create the base dir
        self.utils.create_dir(f"{self.home_dir}/push_to_git_storage")
        # Set the folder path
        folder_path = f"{self.home_dir}{constants.repo_location_storage_path}"
        # Create the storage dir
        self.utils.create_dir(folder_path)

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

    def handle_branch_push_to_git(self, base, prefix):
        # Get the current repo directory path. Then parse the data to retrieve only the
        # directory name
        curr_repo = self.stored_dir_dropdown.currentText()
        curr_repo_name = curr_repo.rsplit('/', 1)[1]

        # Set the folders path
        dates_storage_path = f"{self.home_dir}{constants.dates_time_storage_path}"
        curr_repo_folder_path = f"{dates_storage_path}/{curr_repo_name}"
        prefix_folder_path = f"{curr_repo_folder_path}/{prefix}"

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

        # Create the storage file, and checks what the version number should be
        dates_storage_file = self.utils.create_or_read_file(
            full_path_to_prefix_file)
        lines = dates_storage_file.readlines()
        version_num = len(lines) + 1
        dates_storage_file.close()

        # Create the branch with a version num
        branch_name = f'{prefix}_{self.utils.current_formatted_date()}v{version_num}'

        with open(full_path_to_prefix_file, 'a+') as my_file:
            my_file.write(f'{branch_name}\n')

        # Change into the repo directory
        os.chdir(curr_repo)

        git_reset_to_base = [
            constants.git,
            constants.reset,
            '--hard',
            f"origin/{base}"
        ]

        git_branch_to_create = [
            constants.git,
            constants.checkout,
            '-b',
            branch_name
        ]

        git_push_branch = [
            constants.git,
            constants.push,
            constants.origin,
            branch_name
        ]

        git_base_branch = [
            constants.git,
            constants.checkout,
            base
            ]

        git_checkout_branch = [
            constants.git,
            constants.checkout,
            prefix
            ]

        processes_to_complete = {
            # Switch to the default branch
            '0': git_base_branch,
            # Fetch the remote's origin
            '1': constants.git_fetch_origin,
            # Now switch to the branch where you want to push data to git
            '2': git_checkout_branch,
            # Now create a unique branch based off the above branch
            '3': git_branch_to_create,
            # Push the newly creted branch to github.  This will be our copy
            # in case anything goes wrong with the merge
            '4': git_push_branch,
            # Return to the branch that we switched to (not the base branch)
            '5': git_checkout_branch,
            # Now lets match the branch we switched to to the base branch
            '6': git_reset_to_base,
            # And push the branch to github
            '7': constants.git_push_origin
        }

        for key in processes_to_complete:
            git_process = processes_to_complete[key]
            current_branch = subprocess.Popen(git_process)
            current_branch.wait()
