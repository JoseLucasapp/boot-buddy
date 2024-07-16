class Generate_select:
    def __init__(self, type, message, name, choices=[], default=True):
        self.type = type
        self.message = message
        self.name = name

        if type == 'list':
            self.choices = choices
        elif type == 'confirm':
            self.default = default

    def generate(self):
        options = {
            "type": self.type,
            "message": self.message,
            "name": self.name
        }

        if self.type == 'list':
            options['choices'] = self.choices
        elif self.type == 'confirm':
            options['default'] = self.default

        return options
