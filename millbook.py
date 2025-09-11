#!/user/bin/env/ python3

import sys
from PySide6.QtWidgets import (
    QApplication,
)

from WelcomeDialog import WelcomeDialog
from MainWindow import MainWindow


class Milbook():

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = None
        self.project = None
        pass

    def run(self):
        self.main_window = MainWindow()
        self.main_window.show()

        welcomeDialog = WelcomeDialog()
        welcomeDialog.exec()


        return self.app.exec()
        
        pass


if __name__ == "__main__":
    app = Milbook()
    app.run()
