from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QLineEdit, QGroupBox, QFormLayout, QVBoxLayout,
    QHBoxLayout, QStyle, QPushButton, QListView
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mil Book")
        self.resize(600, 400)
        self.wrapper = QWidget()
        self.main = QHBoxLayout()
        self.wrapper.setLayout(self.main)
        self.setCentralWidget(self.wrapper)
        self._create_menus()
        self._project_settings_ui()
        pass


    def _create_menus(self):
        menu = self.menuBar()
        self._file_menu(menu)
        pass

    def _file_menu(self, mb):
        file_menu = mb.addMenu("File")
        new_project = QAction("New Project", self)
        load_project = QAction("Load Project", self)
        file_menu.addAction(new_project)
        file_menu.addAction(load_project)
        pass

    def _project_settings_ui(self):

        file_settings_group = QGroupBox("File Settings")
        file_settings_form = QFormLayout()

        icon = self.style().standardIcon(QStyle.StandardPixmap.SP_DirOpenIcon)
        source_path = QHBoxLayout()
        source_path.addWidget(QLineEdit())
        source_path.addWidget(QPushButton(icon, ""))
        
        dest_path = QHBoxLayout()
        dest_path.addWidget(QLineEdit())
        dest_path.addWidget(QPushButton(icon, ""))


        file_settings_form.addRow("Source Path", source_path)
        file_settings_form.addRow("Destination Path", dest_path)
        file_settings_form.addRow("File Name", QLineEdit())
        file_settings_group.setLayout(file_settings_form)

        project_settings_group = QGroupBox("Project Settings")
        project_settings_form = QFormLayout()
        project_settings_form.addRow("Title", QLineEdit())
        project_settings_form.addRow("Author", QLineEdit())
        project_settings_form.addRow("Date", QLineEdit())
        project_settings_group.setLayout(project_settings_form)

        settings_layout = QVBoxLayout()
        settings_layout.addWidget(file_settings_group)
        settings_layout.addWidget(project_settings_group)
        settings_layout.addWidget(QPushButton("Load"))
        settings_layout.addWidget(QPushButton("Generate"))

    
        self.main.addLayout(settings_layout)


        projec_list = QListView()

        self.main.addWidget(projec_list)




        pass
