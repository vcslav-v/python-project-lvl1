"""Prime game."""

from math import sqrt
from random import randint

from brain_games import config


def is_prime(number):
    """Check is number prime.

    Parameters:
        number:int

    Returns:
        bool
    """
    if number < 2:
        return False
    for divider in range(2, int(sqrt(number)) + 1):
        if number % divider == 0:
            return False
    return True


def questions_generator():
    """Generate quest/answer for Prime game.

    Returns:
        tuple
    """
    number = randint(  # noqa: S311
        config.MIN_NUMBER_FOR_PRIME_GAME,
        config.MAX_NUMBER_FOR_PRIME_GAME,
        )
    if is_prime(number):
        answer = config.YES_ANSWER
    else:
        answer = config.NO_ANSWER
    return str(number), answer
