from models.access_apps import Access_apps
from src.prompt_messages import Prompt_messages
from src.system_settings import System_settings
from src.prints import Prints
from src.links import Links


class Apps:
    def __init__(self):
        self.prompt_messages = Prompt_messages
        self.access_apps_model = Access_apps
        self.system_settings = System_settings
        self.prints = Prints
        self.add_link = Links().add_link

    def add_apps(self, access_pattern_id):
        self.prints.app_path_hint()
        while True:
            access_apps_prompt = self.prompt_messages.add_new_app_message()
            with self.system_settings.get_current_app().app_context():
                access_apps_data = self.access_apps_model.add(name=access_apps_prompt['app_name'],
                                                              access_patterns_id=access_pattern_id,
                                                              path=access_apps_prompt['app_path'],
                                                              is_browser=access_apps_prompt['is_browser'])

                if access_apps_prompt['is_browser']:
                    self.add_link(access_apps_data)

            add_next_prompt = self.prompt_messages.add_next('app')
            if add_next_prompt['next'] == False:
                break

    def to_open_apps(self, app_path):
        try:
            self.system_settings.start_file(app_path)
        except:
            self.prints.verify_your_path(app_path)
