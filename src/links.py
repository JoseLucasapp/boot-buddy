from models.access_links import Access_links
from src.prompt_messages import Prompt_messages
from src.system_settings import System_settings
from src.prints import Prints


class Links:
    def __init__(self):
        self.prompt_messages = Prompt_messages
        self.access_links_model = Access_links
        self.system_settings = System_settings
        self.prints = Prints

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

    def to_open_links(self, app_path, links):

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
