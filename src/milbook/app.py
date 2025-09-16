#!/user/bin/env/ python3

import sys
from PySide6.QtWidgets import (
    QApplication,
)
from .core.project_handler import ProjectLoader
from .ui.WelcomeDialog import WelcomeDialog
from .ui.MainWindow import MainWindow


class Milbook():

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = MainWindow()
        self.welcome_window = WelcomeDialog()
        self.project_path = None
        self.connect_actions()
        pass



    def run(self):
        self.main_window.show()

        welcomeDialog = WelcomeDialog()
        welcomeDialog.exec()


        return self.app.exec()
        
        pass


