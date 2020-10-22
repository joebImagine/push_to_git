from PySide2.QtCore import Qt, Slot
from PySide2.QtWidgets import (
    QApplication, QWidget, QFileDialog
)
from pathlib import Path

class PushToGitSlots(QWidget):
    @Slot()
    def exit_app(self, checked):
        QApplication.quit()

    @Slot()
    def show_dialog(self):
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)
