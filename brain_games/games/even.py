"""Even or not game."""

from random import randint

from brain_games import config

MIN_NUMBER = -100
MAX_NUMBER = 100
INSTRUCTION = (
    'Answer "{yes}" if number even otherwise answer "{no}".'
).format(yes=config.YES_ANSWER, no=config.NO_ANSWER)


def get_round_data() -> tuple:
    """Generate quest/answer for even or not game.

    Returns:
        (quest, right answer)
    """
    quest = randint(MIN_NUMBER, MAX_NUMBER)
    if quest % 2 == 0:
        answer = config.YES_ANSWER
    else:
        answer = config.NO_ANSWER
    return quest, answer
