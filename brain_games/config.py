"""Config file."""

HELLO_STRING = 'Welcome to the Brain Games!'
HELLO_NAME_STRING = 'Hello, {name}!'
ASK_NAME_STRING = 'May I have your name? '
WIN_STRING = 'Congratulations, {name}!'
WRONG_STRING = (
    '{wrong_answer} is wrong answer ;(. Correct answer was {right_answer}.'
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
