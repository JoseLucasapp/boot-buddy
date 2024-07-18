from InquirerPy import prompt

from flask import current_app

from models.access_pattern import Access_pattern


class Prompt_messages:

    def __init__(self) -> None:
        self.selected_stack = ''

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
            self.add_new_stack()
