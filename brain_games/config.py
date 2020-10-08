"""Config file."""

HELLO_PATTERN = 'Welcome to the Brain Games!'
HELLO_NAME_PATTERN = 'Hello, {name}!'
NAME_PATTERN = 'May I have your name? '
WIN_PATTERN = 'Congratulations, {name}!'
WRONG_PATTERN = (
    '{wrong_answer} is wrong answer ;(. Correct answer was {right_answer}.'
)
LOSE_PATTERN = ("Let's try again, {name}!")
QUESTION_PATTERN = 'Question: {quest}'
CORRECT_PATTERN = 'Correct!'
ANSWER_PATTERN = 'Your answer: '
ERROR_PATTERN = 'ERROR'
GAP_STING = '\n\n'

NUMBER_OF_ATTEMPTS = 3

YES_ANSWER = 'yes'
NO_ANSWER = 'no'

RE_ANSWER_PATTERN_YES_OR_NO = '{yes}|{no}'.format(
    yes=YES_ANSWER, no=NO_ANSWER,
)
RE_ANSWER_PATTERN_NUMBER = r'-?\d+'
