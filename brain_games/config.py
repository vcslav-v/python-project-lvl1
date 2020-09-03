"""Config file."""

# region Common settings
HELLO_STRING = 'Welcome to the Brain Games!'
HELLO_NAME_STRING = 'Hello, {name}!'
ASK_NAME_STRING = 'May I have your name? '
WIN_STRING = 'Congratulations, {name}!'
WRONG_STRING = (
    '{wrong_answer} is wrong answer ;(.' +
    ' Correct answer was {right_answer}.'
    )
LOSE_STRING = ("Let's try again, {name}!")
QUESTION_STRING = 'Question: {quest}'
CORRECT_STRING = 'Correct!'
ASK_ANSWER_STRING = 'Your answer: '
ERROR_STRING = 'ERROR'
GAP_STING = '\n\n'

NUMBER_OF_ATTEMPTS = 3

YES_ANSWER = 'yes'
NO_ANSWER = 'no'

RE_ANSWER_PATTERN_YES_OR_NO = '{yes}|{no}'.format(
    yes=YES_ANSWER, no=NO_ANSWER,
    )
RE_ANSWER_PATTERN_NUMBER = r'-?\d+'
# endregion

# region "Even or not" game settings
MIN_NUMBER_FOR_QUESTION_EVEN_OR_NOT_GAME = -100
MAX_NUMBER_FOR_QUESTION_EVEN_OR_NOT_GAME = 100
INSTRUCTION_STRING_EVEN_OR_NOT_GAME = (
    'Answer "{yes}" if number ' +
    'even otherwise answer "{no}".'
    ).format(yes=YES_ANSWER, no=NO_ANSWER)
# endregion

# region "Calculator" game settings
INSTRUCTION_STRING_CALC_GAME = 'What is the result of the expression?'
MIN_NUMBER_FOR_CALCULATOR_GAME = 0
MAX_NUMBER_FOR_CALCULATOR_GAME = 20
OPERATIONS = {  # noqa: WPS407
    '+': lambda num1, num2: num1+num2,
    '-': lambda num1, num2: num1-num2,
    '*': lambda num1, num2: num1*num2,
    }
QUEST_EVAL_STRING = '{num1} {operation} {num2}'
# endregion

# region "GCD" game settings
INSTRUCTION_STRING_GCD_GAME = (
    'Find the greatest common divisor of given numbers.'
    )
MIN_NUMBER_FOR_GCD_GAME = 0
MAX_NUMBER_FOR_GCD_GAME = 100
QUEST_GDC_STRING = '{num1} {num2}'
# endregion

# region "Progression" game settings
INSTRUCTION_STRING_PROGRESSION_GAME = (
    'What number is missing in the progression?'
)
MIN_DIFF_FOR_PROGRESSION_GAME = 1
MAX_DIFF_FOR_PROGRESSION_GAME = 10
MIN_START_FOR_PROGRESSION_GAME = 0
MAX_START_FOR_PROGRESSION_GAME = 10
LENGTH_OF_PROGRESSION = 10
ELEMENT_OF_PROGRESSION = '{element} '
LOSE_ELEMENT = '..'
# endregion

# region "Prime" game settings
INSTRUCTION_STRING_PRIME_GAME = (
    'Answer "{yes}" if given number is prime. ' +
    'Otherwise answer "{no}".'
).format(yes=YES_ANSWER, no=NO_ANSWER)
MIN_NUMBER_FOR_PRIME_GAME = 1
MAX_NUMBER_FOR_PRIME_GAME = 1000
# endregion
