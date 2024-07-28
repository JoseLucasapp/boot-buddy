from models.access_pattern import Access_pattern
from models.access_apps import Access_apps
from models.access_links import Access_links
from src.prompt_messages import Prompt_messages
from src.system_settings import System_settings
from src.prints import Prints
from src.apps import Apps
from src.links import Links


class Stack:
    def __init__(self):
        self.prompt_messages = Prompt_messages
        self.access_apps_model = Access_apps
        self.access_links_model = Access_links
        self.access_patterns_model = Access_pattern
        self.open_apps = Apps().to_open_apps
        self.open_links = Links().to_open_links
        self.system_settings = System_settings
        self.back_to_menu = True
        self.prints = Prints
        self.add_apps = Apps().add_apps

    def delete_stack(self, pattern_id):
        delete_stack_prompt = self.prompt_messages.delete_stack()
        if delete_stack_prompt['delete_stack']:
            app_ids = self.access_apps_model.get_by_pattern_id(pattern_id)
            self.access_apps_model.delete_apps_by_pattern(pattern_id)
            for app_id in app_ids:
                self.access_links_model.delete_links_by_app(app_id['id'])

            self.access_patterns_model.delete_pattern(pattern_id=pattern_id)
            self.back_to_menu = True
        else:
            self.back_to_menu = False

    def add_stack(self):
        stack_prompt = self.prompt_messages.add_stack_message()
        with self.system_settings.get_current_app().app_context():
            data = self.access_patterns_model.add(stack_prompt['stack_name'],
                                                  stack_prompt['stack_description'])
            self.add_apps(data.id)

    def select_stack(self, stack):
        access_apps = self.access_apps_model.get_by_pattern_id(stack['id'])
        self.prints.apps_on_stack(stack["name"])
        for app in access_apps:
            if app['is_browser']:
                self.prints.app_name(app["name"])
                access_links = self.access_links_model.get_by_app_id(app['id'])
                for link in access_links:
                    self.prints.link_name(link["link_name"])
            else:
                self.prints.app_name(app["name"])

        open_stack = self.prompt_messages.open_stack_apps_message()

        if open_stack['open_stack']:
            for app in access_apps:
                if app['is_browser']:
                    access_links = self.access_links_model.get_by_app_id(
                        app['id'])
                    self.open_links(app['path'], access_links)
                else:
                    self.open_apps(app['path'])
        else:
            back_to_menu = self.prompt_messages.back_to_menu()
            if back_to_menu['back_to_menu']:
                self.back_to_menu = True
            else:
                self.delete_stack(stack['id'])

    def main(self):
        choices = []
        already_created_stacks = self.access_patterns_model.get()
        for created_stack in already_created_stacks:
            choices.append(created_stack['name'])
        choices.append('Add new stack')
        choices.append('Quit')

        selected_stack = self.prompt_messages.stack_message(choices=choices)

        if selected_stack['stack'] == 'Add new stack':
            self.add_stack()
        elif selected_stack['stack'] == 'Quit':
            self.system_settings.quit_app()

        for created_stack in already_created_stacks:
            if selected_stack['stack'] == created_stack['name']:
                self.select_stack(created_stack)
