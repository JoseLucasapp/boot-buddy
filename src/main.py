from flask import current_app

from models.access_pattern import Access_pattern
from models.access_apps import Access_apps
from models.access_links import Access_links

from src.open_apps import Open_apps
from src.open_links import Open_links

from src.prompt_messages import Prompt_messages


class Booty_buddy:

    def __init__(self):
        self.prompt_messages = Prompt_messages
        self.access_apps_model = Access_apps
        self.access_links_model = Access_links
        self.access_patterns_model = Access_pattern
        self.open_apps = Open_apps
        self.open_links = Open_links

    def add_link(self, access_apps_data):
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

        if open_stack['open_stack']:
            for app in access_apps:
                if app['is_browser']:
                    access_links = self.access_links_model.get_by_app_id(
                        app['id'])
                    self.open_links(app['path'], access_links)
                else:
                    self.open_apps(app['path'])

    def stack(self):
        choices = []
        already_created_stacks = self.access_patterns_model.get()
        for created_stack in already_created_stacks:
            choices.append(created_stack['name'])
        choices.append('Add new stack')

        selected_stack = self.prompt_messages.stack_message(choices=choices)

        if selected_stack['stack'] == 'Add new stack':
            self.add_stack()

        for created_stack in already_created_stacks:
            if selected_stack['stack'] == created_stack['name']:
                self.select_stack(created_stack)
