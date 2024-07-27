from src.prints import Prints
from src.system_settings import System_settings


class Open_links:
    def __init__(self, app_path, links):
        self.prints = Prints
        self.system_settings = System_settings

        for link in links:
            try:
                url = link.get('link', '')
                if url:
                    command = f'"{app_path}" {url}'
                    self.system_settings.call_command(command=command)
                else:
                    self.prints.no_valid_url()
            except Exception as e:
                self.prints.error_openning(link, e)
