class Prints:
    def app_path_hint():
        print(' ')
        print('Add app(s) to your stack:')
        print(' ')
        print('Hint: You can use the command which <app_name> to find your app path on Linux, and where <app_name> on Windows')

    def no_valid_url():
        print("Error: No valid URL found in the link dictionary.")

    def error_openning(target, error):
        print(f"Error opening {target}: {error}")

    def verify_your_path(app_path):
        print(f'Verify your path: {app_path}')

    def apps_on_stack(stack_name):
        print(f'This is the list of apps on {stack_name} stack:')

    def app_name(app_name):
        print(f'-- {app_name}:')

    def link_name(link_name):
        print(f'    > {link_name}')
