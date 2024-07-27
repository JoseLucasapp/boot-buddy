from InquirerPy import prompt


class Prompt_messages:

    def stack_message(choices):
        return prompt([
            {
                "type": "list",
                "message": "Which stack you want to open:",
                "name": "stack",
                "choices": choices
            }
        ])

    def add_stack_message():
        return prompt([
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
        ])

    def add_new_app_message():
        example_windows_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        message = f"What is the path of the app \nfor example chrome in Windows: {example_windows_path}\nchrome in Linux: /usr/bin/google-chrome)?"

        return prompt([
            {
                "type": "input",
                "message": "What is the name of the app?",
                "name": "app_name",
            },
            {
                "type": "input",
                "message": message,
                "name": "app_path",
            },
            {
                "type": 'confirm',
                "message": 'Is it an browser?',
                "name": 'is_browser',
                "default": False,
            }
        ])

    def add_new_app_link():
        return prompt([
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
        ])

    def add_next(next):
        message = f'Do you want to add other {next}?'
        return prompt([
            {
                "type": 'confirm',
                "message": message,
                "name": 'next',
                "default": True,
            }
        ])

    def open_stack_apps_message():
        return prompt([
            {
                "type": 'confirm',
                "message": 'Do you want to open this stack?',
                "name": 'open_stack',
                "default": False,
            }
        ])

    def want_to_add_links():
        return prompt([
            {
                "type": 'confirm',
                "message": 'Do you want to add links to your browser?',
                "name": 'to_add_link',
                "default": True,
            }
        ])

    def back_to_menu():
        return prompt([
            {
                "type": 'confirm',
                "message": 'Do you want to move back to menu?',
                "name": 'back_to_menu',
                "default": True,
            }
        ])
