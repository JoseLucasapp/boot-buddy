import os
import sys
from flask import current_app


class System_settings:
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

    def quit_app():
        sys.exit(0)

    def call_command(command):
        os.system(command)

    def start_file(file_path):
        os.startfile(file_path)

    def get_current_app():
        return current_app
