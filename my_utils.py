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
        currentMonth = current_date.strftime("%m")
        currentYear = current_date.strftime("%Y")

        return f'{currentYear}{currentMonth}{current_day}'

    def create_file(self, path_name):
        if not os.path.exists(path_name):
            return open(path_name, "w+")

    def create_or_read_file(self, path_name):
        if os.path.exists(path_name):
            return open(path_name, "r")
        else:
            self.create_file()

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
        self.create_dir(folder_path)
        full_path = f"{folder_path}/{constants.list_items_file_name}"

        # Write the directory path to the file
        with open(full_path, 'a+') as my_storage_items:
            my_storage_items.write(f'{curr_dir}\n')
