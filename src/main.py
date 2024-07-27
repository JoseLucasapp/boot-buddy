from flask import current_app

from models.access_pattern import Access_pattern
from models.access_apps import Access_apps
from models.access_links import Access_links

from src.open_apps import Open_apps
from src.open_links import Open_links

from src.prompt_messages import Prompt_messages
from src.system_settings import System_settings


class Booty_buddy:

    def __init__(self):
        self.prompt_messages = Prompt_messages
        self.access_apps_model = Access_apps
        self.access_links_model = Access_links
        self.access_patterns_model = Access_pattern
        self.open_apps = Open_apps
        self.open_links = Open_links
        self.system_settings = System_settings
        self.back_to_menu = True

    def add_link(self, access_apps_data):
        want_to_add_links = self.prompt_messages.want_to_add_links()

        if want_to_add_links['to_add_link']:
            while True:
                add_new_app_link_prompt = self.prompt_messages.add_new_app_link()

                with current_app.app_context():
                    self.access_links_model.add(link=add_new_app_link_prompt['link_url'],
                                                link_name=add_new_app_link_prompt['link_name'],
                                                access_apps_id=access_apps_data.id)

                add_next_prompt = self.prompt_messages.add_next('link')

                if add_next_prompt['next'] == False:
                    break

    def add_apps(self, access_pattern_id):
        print(' ')
        print('Add app(s) to your stack:')
        print(' ')
        print('Hint: You can use the command which <app_name> to find your app path on Linux, and where <app_name> on Windows')
        while True:
            access_apps_prompt = self.prompt_messages.add_new_app_message()

            with current_app.app_context():
                access_apps_data = self.access_apps_model.add(name=access_apps_prompt['app_name'],
                                                              access_patterns_id=access_pattern_id,
                                                              path=access_apps_prompt['app_path'],
                                                              is_browser=access_apps_prompt['is_browser'])

                if access_apps_prompt['is_browser']:
                    self.add_link(access_apps_data)

            add_next_prompt = self.prompt_messages.add_next('app')

            if add_next_prompt['next'] == False:
                break

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

        with current_app.app_context():
            data = self.access_patterns_model.add(stack_prompt['stack_name'],
                                                  stack_prompt['stack_description'])
            self.add_apps(data.id)

    def select_stack(self, stack):
        access_apps = self.access_apps_model.get_by_pattern_id(stack['id'])
        print(f'This is the list of apps on {stack["name"]} stack:')
        for app in access_apps:
            if app['is_browser']:
                print(f'-- {app["name"]}:')
                access_links = self.access_links_model.get_by_app_id(app['id'])
                for link in access_links:
                    print(f'    > {link["link_name"]}')
            else:
                print(f'-- {app["name"]}')

        open_stack = self.prompt_messages.open_stack_apps_message()
        back_to_menu = self.prompt_messages.back_to_menu()

        if open_stack['open_stack']:
            for app in access_apps:
                if app['is_browser']:
                    access_links = self.access_links_model.get_by_app_id(
                        app['id'])
                    self.open_links(app['path'], access_links)
                else:
                    self.open_apps(app['path'])
        else:
            if back_to_menu['back_to_menu']:
                self.back_to_menu = True
            else:
                self.delete_stack(stack['id'])

    def stack(self):
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

    def main(self):
        while True:
            if self.back_to_menu:
                self.system_settings.clear_terminal()
                self.stack()
            else:
                break
