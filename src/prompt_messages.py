class Prompt_messages:

    def stack_message(choices):
        return [
            {
                "type": "list",
                "message": "Which stack you want to open:",
                "name": "stack",
                "choices": choices
            }
        ]

    def add_stack_message():
        return [
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

    def add_new_app_message():
        return [
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

    def add_new_app_link():
        return [
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

    def add_next_app():
        return [
            {
                "type": 'confirm',
                "message": 'Do you want to add other app?',
                "name": 'next_app',
                "default": False,
            }
        ]

    def open_stack_apps_message():
        return [
            {
                "type": 'confirm',
                "message": 'Do you want to open this stack?',
                "name": 'open_stack',
                "default": False,
            }
        ]
