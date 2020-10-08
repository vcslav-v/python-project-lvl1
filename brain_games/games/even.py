"""Even or not game."""

from random import randint

MIN_NUMBER = -100
MAX_NUMBER = 100
INSTRUCTION = 'Answer "yes" if number even otherwise answer "no".'


def get_round_data() -> tuple:
    """Generate quest/answer for even or not game.

    Returns:
        (quest, right answer)
    """
    quest = randint(MIN_NUMBER, MAX_NUMBER)
    if quest % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return quest, answer
