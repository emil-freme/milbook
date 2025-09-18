import os
import glob
import subprocess
import shutil
import platform
from pathlib import Path
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QStandardItemModel, QStandardItem
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QLineEdit, QGroupBox, QFormLayout, QVBoxLayout,
    QHBoxLayout, QStyle, QPushButton, QListView, QFileDialog
)

from ..core.data import ProjectData


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mil Book")
        self.resize(600, 400)
        self.wrapper = QWidget()
        self.main = QHBoxLayout()
        self.wrapper.setLayout(self.main)
        self.setCentralWidget(self.wrapper)

        self.selected_type = None
        self.project_path = None

        self.source_path_input = QLineEdit()
        self.dest_path_input = QLineEdit()
        self.out_name_input = QLineEdit()
        self.author_name_input = QLineEdit()
        self.tile_input = QLineEdit()
        self.date_input = QLineEdit()

        self._create_menus()
        self._project_settings_ui()

        pass  # __init__


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

        new_project.triggered.connect(self.on_new_click)
        load_project.triggered.connect(self.on_load_click)

        pass  # _file_menu

    def _project_settings_ui(self):

        file_settings_group = QGroupBox("File Settings")
        file_settings_form = QFormLayout()

        icon = self.style().standardIcon(QStyle.StandardPixmap.SP_DirOpenIcon)
        source_path = QHBoxLayout()
        source_path.addWidget(self.source_path_input)
        source_path.addWidget(QPushButton(icon, ""))
        
        dest_path = QHBoxLayout()
        dest_path.addWidget(self.dest_path_input)
        dest_path.addWidget(QPushButton(icon, ""))


        file_settings_form.addRow("Source Path", source_path)
        file_settings_form.addRow("Destination Path", dest_path)
        file_settings_form.addRow("File Name", self.out_name_input)
        file_settings_group.setLayout(file_settings_form)

        project_settings_group = QGroupBox("Project Settings")
        project_settings_form = QFormLayout()
        project_settings_form.addRow("Title", self.tile_input)
        project_settings_form.addRow("Author", self.author_name_input)
        project_settings_form.addRow("Date", self.date_input)
        project_settings_group.setLayout(project_settings_form)

        settings_layout = QVBoxLayout()
        settings_layout.addWidget(file_settings_group)
        settings_layout.addWidget(project_settings_group)


        btn_load_files = QPushButton("Load Files")
        btn_load_files.clicked.connect(self.on_load_files_click)
        settings_layout.addWidget(btn_load_files)

        self.btn_generate = QPushButton("Generate")
        self.btn_generate.clicked.connect(self.on_generate_click)
        self.btn_generate.setEnabled(False)
        settings_layout.addWidget(self.btn_generate)

    
        self.main.addLayout(settings_layout)


        self.projec_list = QListView()

        self.main.addWidget(self.projec_list)

        self.project_data = ProjectData()


        pass  # _project_settings_ui

    
    def reload_ui(self):
        self.source_path_input.setText(self.project_data.src_path)
        self.dest_path_input.setText(self.project_data.out_path)
        self.out_name_input.setText(self.project_data.out_name)
        self.author_name_input.setText(self.project_data.author_name)
        self.tile_input.setText(self.project_data.project_title)
        self.date_input.setText(self.project_data.project_date)
        
        pass  # reload_ui

        
    
    def on_load_click(self):
        fileName, _ = QFileDialog.getOpenFileName(self,
                 "Selecione o arquivo do projeto",
                 "~",
                 "Milbook Project Files (*.mil);;Legacy Config Files (*.ini)"
                 )

        if (fileName is None):
            self.reject()
        self.project_data.project_settings = fileName
        self.project_data.load_project()
        self.reload_ui()

        pass  # on_load_click

    
    def on_new_click(self):
        dirName = QFileDialog.getExistingDirectory(self,
                 "Selecione o diretório do projeto",
                 "~",
                 )

        if (dirName is not None):
            self.reject()

        self.projectData.src_path = dirName

        pass  # on_new_click

    
    def on_load_files_click(self):
        # https://stackoverflow.com/questions/846684/a-listview-of-checkboxes-in-pyqt
        model = QStandardItemModel()

        files = sorted(Path(self.source_path_input.text()).glob("*.md"))
        for file in files:
            item = QStandardItem()
            item.setData(file, Qt.UserRole)
            item.setText(file.stem)
            item.setCheckable(True)
            item.setCheckState(Qt.Checked)
            model.appendRow(item)

        self.projec_list.setModel(model)
        self.btn_generate.setEnabled(True)
        pass

    
    def on_generate_click(self):
        model = self.projec_list.model()
        with open("content.md", "w", encoding="utf-8") as content:
            for i in range(model.rowCount()):
                item = model.item(i)
                if (item.checkState() != Qt.Checked):
                    continue
                file = item.data(Qt.UserRole)
                print(file)
                with open(f"{file}", "r", encoding="utf-8") as temp:
                    shutil.copyfileobj(temp, content)
                    content.write("\n\n")
                    pass
            pass
        pass

        project_root = Path.cwd()
        resources_path = project_root.joinpath("src", "milbook", "resources")

        frontmatter_yaml = f"""---
author: "{self.author_name_input.text()}"
title: "{self.tile_input.text()}"
date: "{self.date_input.text()}"
graphicspath: "{Path(self.source_path_input.text()).resolve().as_posix()}"
---
"""
        
        print("Prepending frontmatter")
        with open("prepared.md", "w", encoding="utf-8") as prepared:
            prepared.write(frontmatter_yaml)
            with open("content.md", "r", encoding="utf-8") as content:
                shutil.copyfileobj(content, prepared)
            pass
        pass
        
        print(resources_path)
        print("Generating tex file")
        pandoc_command = ["pandoc",
             "--verbose",
             "--template",
             str(resources_path.joinpath("tex", "main.tex").resolve()),
             "--top-level-division", "chapter",
             "--lua-filter",
             str(resources_path.joinpath("lua", "minted.lua").resolve()),
             "--lua-filter",
             str(resources_path.joinpath("lua", "div2latexenv.lua").resolve()),
             "prepared.md",
             "-o", "out.tex"]

        print(pandoc_command)
        subprocess.run(pandoc_command)

        print("Generating PDF")
        subprocess.run(["xelatex", "-shell-escape", "out.tex"])
        # Run two time to get references right
        subprocess.run(["xelatex", "-shell-escape", "out.tex"])

        # print("Cleanup")
        # cleanup_files = glob.glob("out.*")
        # for cf in cleanup_files:
        #     os.remove(cf)
        #
        # os.remove("prepared.md")
        # os.remove("content.md")

        system = platform.system()
        if system == 'Darwin':  # macOS
            subprocess.call(['open', "out.pdf"])  # [web:6]
        elif system == 'Windows':
            os.startfile("out.pdf")  # [web:6][web:7]
        else:  # Linux and other *NIX
            subprocess.call(['xdg-open', "out.pdf"])  # [web:2][web:6]
        pass

