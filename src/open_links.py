import os


class Open_links:
    def __init__(self, app_path, links):
        for link in links:
            try:
                url = link.get('link', '')
                if url:
                    command = f'"{app_path}" {url}'
                    os.system(command)
                else:
                    print("Error: No valid URL found in the link dictionary.")
            except Exception as e:
                print(f"Error opening {link}: {e}")
