"""Prime game."""

from math import sqrt
from random import randint

from brain_games import config

MIN_NUMBER = 1
MAX_NUMBER = 1000
INSTRUCTION = (
    'Answer "{yes}" if given number is prime. Otherwise answer "{no}".'
).format(yes=config.YES_ANSWER, no=config.NO_ANSWER)


def is_prime(number: int) -> bool:
    """Check is number prime.

    Parameters:
        number: Number for prime-number testing

    Returns:
        True if number is prime, False if one not
    """
    if number < 2:
        return False
    for divider in range(2, int(sqrt(number)) + 1):
        if number % divider == 0:
            return False
    return True


def get_round_data() -> tuple:
    """Generate quest/answer for Prime game.

    Returns:
        (quest, right answer)
    """
    quest = randint(MIN_NUMBER, MAX_NUMBER)
    if is_prime(quest):
        answer = config.YES_ANSWER
    else:
        answer = config.NO_ANSWER
    return str(quest), answer
