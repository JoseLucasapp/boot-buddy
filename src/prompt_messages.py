from InquirerPy import prompt


class Prompt_messages:

    def __init__(self) -> None:
        self.selected_stack = ''

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

        return self.selected_stack['stack']

    def add_new_stack(self):
        if self.selected_stack['stack'] == 'Or add new stack':
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

    def caller(self):
        self.stack()
        self.add_new_stack()
