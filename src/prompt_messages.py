from InquirerPy import prompt

from flask import current_app

from models.access_pattern import Access_pattern


class Prompt_messages:

    def __init__(self) -> None:
        self.selected_stack = ''

    def access_apps(self):
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

            access_apps_prompt = prompt(add_new_app)

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

                add_new_app_link_prompt = prompt(add_new_app_link)

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
        access_pattern_db = Access_pattern(
            stack_prompt['stack_name'], stack_prompt['stack_description'])

        with current_app.app_context():
            access_pattern_db.add()

    def stack(self):
        default = [
            {
                "type": "list",
                "message": "Which stack you want to open:",
                "name": "stack",
                "choices": ["Work", "Study", "Or add new stack"]
            }
        ]

        self.selected_stack = prompt(default)

        if self.selected_stack['stack'] == 'Or add new stack':
            # self.add_new_stack()
            self.access_apps()
