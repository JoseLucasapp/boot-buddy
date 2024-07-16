from InquirerPy import prompt
from src.utils import generateSelect

questions = []
programs = generateSelect.Generate_select(
    'list', 'Quais programas você prefere ?', 'programs', ['Chrome', 'Paint', 'VSCode'])

questions.append(programs.generate())

answers = prompt(questions)
print(f'Você escolheu {answers['programs']}')
