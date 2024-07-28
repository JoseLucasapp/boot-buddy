from src.system_settings import System_settings
from src.stack import Stack


class Booty_buddy:
    def __init__(self):
        self.system_settings = System_settings
        self.back_to_menu = True
        self.stack = Stack

    def main(self):
        while True:
            if self.back_to_menu:
                self.system_settings.clear_terminal()
                self.stack().main()
            else:
                break
