from models.access_pattern import Access_pattern
from models.access_apps import Access_apps
from models.access_links import Access_links
from src.open_links import Open_links
from src.prompt_messages import Prompt_messages
from src.system_settings import System_settings
from src.prints import Prints

from src.stack import Stack


class Booty_buddy:
    def __init__(self):
        self.prompt_messages = Prompt_messages
        self.access_apps_model = Access_apps
        self.access_links_model = Access_links
        self.access_patterns_model = Access_pattern
        self.open_links = Open_links
        self.system_settings = System_settings
        self.back_to_menu = True
        self.prints = Prints
        self.stack = Stack

    def add_link(self, access_apps_data):
        want_to_add_links = self.prompt_messages.want_to_add_links()

        if want_to_add_links['to_add_link']:
            while True:
                add_new_app_link_prompt = self.prompt_messages.add_new_app_link()
                with self.system_settings.get_current_app().app_context():
                    self.access_links_model.add(link=add_new_app_link_prompt['link_url'],
                                                link_name=add_new_app_link_prompt['link_name'],
                                                access_apps_id=access_apps_data.id)

                add_next_prompt = self.prompt_messages.add_next('link')
                if add_next_prompt['next'] == False:
                    break

    def main(self):
        while True:
            if self.back_to_menu:
                self.system_settings.clear_terminal()
                self.stack().main()
            else:
                break
