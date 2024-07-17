from src.prompt_messages import Prompt_messages
if __name__ == "__main__":
    prompt_messages = Prompt_messages()
    stack_selection = prompt_messages.stack()

    print(f'Selected stack: {stack_selection}')
