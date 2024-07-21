import os


class Open_apps:
    def __init__(self, app_path) -> None:
        try:
            os.startfile(app_path)
        except:
            print(f'Verify your path: {app_path}')
