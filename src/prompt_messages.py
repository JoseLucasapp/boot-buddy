from InquirerPy import prompt


class Prompt_messages:
    def stack(self):
        default = [
            {
                "type": "list",
                "message": "Which stack you want to open:",
                "name": "stack",
                "choices": ["Work", "Study", "Or add new stack"]
            }
        ]

        answers = prompt(default)

        return answers['stack']
