from InquirerPy import prompt

from flask import current_app

from models.access_pattern import Access_pattern
from models.access_apps import Access_apps
from models.access_links import Access_links

from src.prompt_messages import Prompt_messages


class Booty_buddy:

    def __init__(self):
        self.selected_stack = ''
        self.prompt_messages = Prompt_messages

    def access_apps(self, access_pattern_id):
        while True:
            add_new_app = self.prompt_messages.add_new_app_message()

            print(' ')
            access_apps_prompt = prompt(add_new_app)
            access_apps = Access_apps

            with current_app.app_context():
                access_apps_data = access_apps.add(name=access_apps_prompt['app_name'],
                                                   access_patterns_id=access_pattern_id,
                                                   path=access_apps_prompt['app_path'],
                                                   is_browser=access_apps_prompt['is_browser'])

                if access_apps_prompt['is_browser']:
                    add_new_app_link = self.prompt_messages.add_new_app_link()

                    print(' ')
                    add_new_app_link_prompt = prompt(add_new_app_link)
                    access_links = Access_links

                    with current_app.app_context():
                        access_links.add(link=add_new_app_link_prompt['link_url'],
                                         link_name=add_new_app_link_prompt['link_name'],
                                         access_apps_id=access_apps_data.id)

            add_next_app = self.prompt_messages.add_next_app()

            add_next_app_prompt = prompt(add_next_app)

            if add_next_app_prompt['next_app'] == False:
                break

    def add_new_stack(self):
        add_new_stack_prompt = self.prompt_messages.add_stack_message()

        stack_prompt = prompt(add_new_stack_prompt)
        access_pattern_db = Access_pattern

        with current_app.app_context():
            data = access_pattern_db.add(stack_prompt['stack_name'],
                                         stack_prompt['stack_description'])
            self.access_apps(data.id)

    def stack(self):
        choices = []
        already_created_stacks = Access_pattern.get()
        for created_stack in already_created_stacks:
            choices.append(created_stack['name'])
        choices.append('Add new stack')

        default = self.prompt_messages.stack_message(choices=choices)

        self.selected_stack = prompt(default)

        if self.selected_stack['stack'] == 'Add new stack':
            self.add_new_stack()
