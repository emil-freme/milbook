import configparser
from data import ProjectData

from PySide6.QtWidgets import (
    QFileDialog
)


class ProjectLoader:
    def createNewProject(projectData):
        project_path = QFileDialog.getExistingDirectory(
            "Selecione a pasta do projeto",
            "~"
        )

        assert project_path, "Pasta não selecionada"
        return project_path

    def loadProjectSettings(projectData: ProjectData):
        config = configparser.ConfigParser()
        assert config.read(projectData.projectSettings,
                           encoding="utf=8"
                           ), "Arquivo de configuração invalido"
        


