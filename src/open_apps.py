from src.system_settings import System_settings
from src.prints import Prints


class Open_apps:
    def __init__(self, app_path) -> None:
        self.system_settings = System_settings
        self.prints = Prints
        try:
            self.system_settings.start_file(app_path)
        except:
            self.prints.verify_your_path(app_path)
