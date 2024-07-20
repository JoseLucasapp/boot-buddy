from InquirerPy import prompt

from flask import current_app

from models.access_pattern import Access_pattern
from models.access_apps import Access_apps
from models.access_links import Access_links


class Prompt_messages:

    def __init__(self) -> None:
        self.selected_stack = ''

    def access_apps(self, access_pattern_id):
        while True:
            add_new_app = [
                {
                    "type": "input",
                    "message": "What is the name of the app?",
                    "name": "app_name",
                },
                {
                    "type": "input",
                    "message": "What is the path of the app ('C:\Program Files\Google\Chrome\Application\chrome.exe'), or the executable name ('notepad.exe')?",
                    "name": "app_path",
                },
                {
                    "type": 'confirm',
                    "message": 'Is it an browser?',
                    "name": 'is_browser',
                    "default": False,
                }
            ]

            print(' ')
            access_apps_prompt = prompt(add_new_app)
            access_apps = Access_apps

            with current_app.app_context():
                access_apps_data = access_apps.add(name=access_apps_prompt['app_name'],
                                                   access_patterns_id=access_pattern_id,
                                                   path=access_apps_prompt['app_path'],
                                                   is_browser=access_apps_prompt['is_browser'])

                if access_apps_prompt['is_browser']:
                    add_new_app_link = [
                        {
                            "type": "input",
                            "message": "What is the name of the link?",
                            "name": "link_name",
                        },
                        {
                            "type": "input",
                            "message": "What is the link?",
                            "name": "link_url",
                        }
                    ]

                    print(' ')
                    add_new_app_link_prompt = prompt(add_new_app_link)
                    access_links = Access_links

                    with current_app.app_context():
                        access_links.add(link=add_new_app_link_prompt['link_url'],
                                         link_name=add_new_app_link_prompt['link_name'],
                                         access_apps_id=access_apps_data.id)

            add_next_app = [
                {
                    "type": 'confirm',
                    "message": 'Do you want to add other app?',
                    "name": 'next_app',
                    "default": False,
                }
            ]

            add_next_app_prompt = prompt(add_next_app)

            if add_next_app_prompt['next_app'] == False:
                break

    def add_new_stack(self):
        add_new_stack_prompt = [
            {
                "type": "input",
                "message": "What is the stack name?",
                "name": "stack_name",
            },
            {
                "type": "input",
                "message": "What is the stack description?",
                "name": "stack_description",
            }
        ]

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

        default = [
            {
                "type": "list",
                "message": "Which stack you want to open:",
                "name": "stack",
                "choices": choices
            }
        ]

        self.selected_stack = prompt(default)

        if self.selected_stack['stack'] == 'Add new stack':
            self.add_new_stack()
