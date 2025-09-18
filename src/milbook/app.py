#!/user/bin/env/ python3

import sys
from PySide6.QtWidgets import (
    QApplication, QDialog
)
from .core.data import ProjectData
from .ui.WelcomeDialog import WelcomeDialog
from .ui.MainWindow import MainWindow


class Milbook():

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = MainWindow()
        self.welcome_window = WelcomeDialog()
        self.project_data = ProjectData()
        pass



    def run(self):
        self.main_window.show()

        welcomeDialog = WelcomeDialog()


        if (welcomeDialog.exec() == QDialog.DialogCode.Accepted):
            if self.project_data.project_settings is not None:  # Load Project
                print(f"Loading Project: {self.project_data.project_settings}")
                self.project_data.load_project()
                self.main_window.reload_ui(self.project_data)
                pass
            elif self.project_data.src_path is not None:
                print(f"Creating Project: {self.project_data.src_path}")
                pass





        return self.app.exec()
        
        pass


