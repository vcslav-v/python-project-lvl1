"""Even or not game."""

from random import randint

import prompt

MIN_NUMBER_FOR_QUESTION = -100
MAX_NUMBER_FOR_QUESTION = 100
NUMBER_OF_ATTEMPTS = 3
HELLO_STRING = 'Welcome to the Brain Games!'
HELLO_NAME_STRING = 'Hello, {name}!'
YES_ANSWER = 'yes'
NO_ANSWER = 'no'
INSTRUCTION_STRING = (
    'Answer "{yes}" if number' +
    'even otherwise answer "{no}".'
    ).format(yes=YES_ANSWER, no=YES_ANSWER)
ASK_NAME_STRING = 'May I have your name? '
WIN_STRING = 'Congratulations, {name}!'
LOSE_STRING = "Let's try again, {name}!"
QUESTION_STRING = 'Question: {num}'
CORRECT_STRING = 'Correct!'
ASK_ANSWER_STRING = 'Your answer: '
GAP_STING = '\n\n'


def welcome():
    """Greets the player."""
    print(HELLO_STRING)  # noqa: WPS421
    print(INSTRUCTION_STRING, end=GAP_STING)  # noqa: WPS421


def ask_name():
    """Asks for the player's name.

    Returns:
        str
    """
    name = prompt.string(ASK_NAME_STRING)
    print(HELLO_NAME_STRING.format(name=name), end=GAP_STING)  # noqa: WPS421
    return name


def game(min_number, max_number):
    """Game logic.

    Parameters:
        min_number: minimum number in the game
        max_number: maximum number in the game

    Returns:
        bool
    """
    attempt = 0
    while attempt < NUMBER_OF_ATTEMPTS:
        num = randint(min_number, max_number)  # noqa: S311
        print(QUESTION_STRING.format(num=num))  # noqa: WPS421
        if not check_win(num):
            break
        print(CORRECT_STRING, end=GAP_STING)  # noqa: WPS421
        attempt += 1
    else:
        return True
    return False


def check_win(num):
    """Ask player even or odd, return True if player win or False if lose.

    Parameters:
        num: question number

    Returns:
        bool
    """
    answ = prompt.string(ASK_ANSWER_STRING)
    if num % 2 == 0 and answ == YES_ANSWER:
        return True
    elif num % 2 != 0 and answ == NO_ANSWER:
        return True
    return False


def summary(name, player_result):
    """Print sums up the game.

    Parameters:
        name: player's name
        player_result: player result win or not
    """
    if player_result:
        print(WIN_STRING.format(name=name), end=GAP_STING)  # noqa: WPS421
    else:
        print(LOSE_STRING.format(name=name), end=GAP_STING)  # noqa: WPS421


def start():
    """Start game."""
    welcome()
    name = ask_name()
    summary(name, game(MIN_NUMBER_FOR_QUESTION, MAX_NUMBER_FOR_QUESTION))
