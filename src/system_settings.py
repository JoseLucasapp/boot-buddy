import os


class System_settings:
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')
