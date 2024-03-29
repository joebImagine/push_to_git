import datetime
import os
import sys
from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QPainter, QColor, QPalette
from PySide2.QtWidgets import (
    QAction, QApplication, QLabel, QSpinBox,
    QMainWindow, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget, QGridLayout, QDoubleSpinBox
)
from PySide2.QtCharts import QtCharts
import constants

class Color(QWidget):

    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class Utils():
    def __init__(self):
        super().__init__()

    def current_formatted_date(self):
        current_date = datetime.datetime.now()

        current_day = current_date.strftime("%d")
        current_month = current_date.strftime("%m")
        current_year = current_date.strftime("%Y")

        return f'{current_year}{current_month}{current_day}'

    def get_file_name(self, path):
        return path.rsplit('/', 1)[1]

    def create_file(self, path_to_file_name):
        if not os.path.exists(path_to_file_name):
            return open(path_to_file_name, "w+")

    def create_or_read_file(self, path_to_file_name):
        if os.path.exists(path_to_file_name):
            return open(path_to_file_name, "r")
        else:
            return open(path_to_file_name, "w+")

    def create_dir(self, folder_path):
        if os.path.exists(folder_path):
            print('Directory %s exists' % folder_path)
        else:
            try:
                os.mkdir(folder_path)
            except OSError:
                print("Creation of the directory %s failed" % folder_path)
            else:
                print("Successfully created the directory %s " % folder_path)

    def set_list_item(self, folder_path, curr_dir):
        full_path = f"{folder_path}/{constants.list_items_file_name}"

        # Write the directory path to the file
        with open(full_path, 'a+') as my_storage_items:
            my_storage_items.write(f'{curr_dir}\n')

    def is_duplicate_list_item(self, get_list_items, curr_dir):
        list_items = get_list_items()
        is_dup = False
        for i in range(len(list_items)):
            list_item = list_items[i]
            if list_item == curr_dir:
                is_dup = True
                break

        return is_dup
