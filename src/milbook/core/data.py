import configparser


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class ProjectData(metaclass=Singleton):

    def __init__(self, *,
                 src_path = None,
                 project_settings = None
                 ):

        self.src_path           = None
        self.project_settings   = None
        self.out_path           = None
        self.out_name           = None
        self.author_name        = None
        self.project_title      = None
        self.project_date       = None

    def load_project(self):
        print(f"Loading project from {self.project_settings}")

        config = configparser.ConfigParser()
        if not config.read(self.project_settings, encoding="utf-8"):
            raise ValueError("Project Settings not valid")

        file_settings = config["File Settings"]
        self.src_path = file_settings["src_path"]
        self.out_path = file_settings["out_path"]
        self.out_name = file_settings["out_name"]

        metadata = config["Metadata"]
        self.author_name = metadata["author"]
        self.project_title = metadata["title"]
        self.project_date = metadata["date"]

        print("Loading ended")



