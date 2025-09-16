from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog, QPushButton, QHBoxLayout, QVBoxLayout, QListView,
    QFileDialog
)


class WelcomeDialog(QDialog):
    def __init__(self):
        super().__init__(None)
        self.selected_type = None
        self.selected_path = None
        self.setWindowFlags(Qt.WindowType.Dialog |
                            Qt.WindowType.FramelessWindowHint
                            )
        self.main_layout = QHBoxLayout(self)
        self.btns = QVBoxLayout()
        self.btn_new = QPushButton("New Project")
        self.btn_load = QPushButton("Load Project")
        self.btn_close = QPushButton("Close")
        self.btns.addWidget(self.btn_new)
        self.btns.addWidget(self.btn_load)
        self.btns.addWidget(self.btn_close)
        self.btns.addStretch()
        self.projec_list = QListView()
        self.main_layout.addLayout(self.btns)
        self.main_layout.addWidget(self.projec_list)
        pass

    def newProject(self):
        project_path = QFileDialog.getExistingDirectory(self,
                               "Selecinar Pasta do Projeto",
                               "~"
                               )
        if (project_path):
            self.selected_type = "new"
            self.selected_path = project_path
            self.accept()
        pass

    def loadProject(self):
        project_path = QFileDialog.getOpenFileName(self,
                                                   "Selecinar Projeto",
                                                   "~", 
                                                   "Projeto (*.mil *.ini)"
                                                   )
        if (project_path):
            self.selected_type = "load"
            self.selected_path = project_path
            self.accept()
        pass

    def close(self):
        self.reject()
        pass
