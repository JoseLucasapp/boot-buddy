import os
import sys


class System_settings:
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

    def quit_app():
        sys.exit(0)
