
from project_handler import ProjectLoader

class ProjectData:

    def __init__(self, *,
                 src_path = None,
                 project_settings = None
                 ):

        assert (src_path is not None or
                project_settings is not None
                ), "Pasta e projeto inexistente"

        self.src_path           = None
        self.project_settings   = None
        self.out_path           = None,
        self.out_name           = None,
        self.author_name        = None,
        self.project_title      = None,
        self.project_date       = None,

        if project_settings is not None:
            ProjectLoader.loadProjectSettings(self)
        else:
            self.createNewProject()

        pass  # __init__
