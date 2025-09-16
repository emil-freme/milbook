from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QDialog, QPushButton, QHBoxLayout, QVBoxLayout, QListView,
    QFileDialog
)

from ..core.data import ProjectData


class WelcomeDialog(QDialog):
    def __init__(self):
        super().__init__(None)

        self.setWindowFlags(Qt.WindowType.Dialog |
                            Qt.WindowType.FramelessWindowHint
                            )

        self.btns = QVBoxLayout()

        self.btn_new = QPushButton("New Project")
        self.btns.addWidget(self.btn_new)
        
        self.btn_load = QPushButton("Load Project")
        self.btns.addWidget(self.btn_load)
        
        self.btn_close = QPushButton("Close")
        self.btns.addWidget(self.btn_close)

        self.btns.addStretch()

        self.projec_list = QListView()

        self.main_layout = QHBoxLayout(self)
        self.main_layout.addLayout(self.btns)
        self.main_layout.addWidget(self.projec_list)
        
        self.bind_buttons()
        self.projectData = ProjectData()
        pass

    def bind_buttons(self):
 
        self.btn_close.clicked.connect(self.on_close)

        self.btn_load.clicked.connect(self.on_load_click)

        self.btn_new.clicked.connect(self.on_new_click)

    def on_close(self):
        self.reject()
        pass

    def on_load_click(self):
        fileName, _ = QFileDialog.getOpenFileName(self,
                 "Selecione o arquivo do projeto",
                 "~",
                 "Milbook Project Files (*.mil);;Legacy Config Files (*.ini)"
                 )

        if (fileName is not None):
            self.reject()
        self.projectData.project_settings = fileName
        self.accept()

        pass

    
    def on_new_click(self):
        dirName = QFileDialog.getExistingDirectory(self,
                 "Selecione o diretório do projeto",
                 "~",
                 )

        if (dirName is not None):
            self.reject()

        self.projectData.src_path = dirName
        self.accept()

        pass
