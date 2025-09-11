from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog, QPushButton, QHBoxLayout, QVBoxLayout, QListView
)


class WelcomeDialog(QDialog):
    def __init__(self):
        super().__init__(None)
        self.setWindowFlags(Qt.WindowType.Popup)
        main_layout = QHBoxLayout(self)
        btns = QVBoxLayout()
        btn_new = QPushButton("New Project")
        btn_load = QPushButton("Load Project")
        btns.addWidget(btn_new)
        btns.addWidget(btn_load)
        btns.addStretch()
        projec_list = QListView()
        main_layout.addLayout(btns)
        main_layout.addWidget(projec_list)
        pass
