"""Prime game."""

from math import sqrt
from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 1000
INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


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
        answer = 'yes'
    else:
        answer = 'no'
    return str(quest), answer
