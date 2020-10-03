"""GCD game."""

from random import randint

INSTRUCTION = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 0
MAX_NUMBER = 100


def gdc(num1: int, num2: int) -> int:
    """Find greatest common divisor for 2 numbers.

    Parameters:
        num1: First number
        num2: Second number

    Returns:
        Greatest common divisor
    """
    if num2 == 0:
        return num1
    return gdc(num2, num1 % num2)


def get_round_data() -> tuple:
    """Generate quest/answer for GDC game.

    Returns:
        (quest, right answer)
    """
    num1 = randint(MIN_NUMBER, MAX_NUMBER)
    num2 = randint(MIN_NUMBER, MAX_NUMBER)
    answer = str(gdc(num1, num2))
    quest = '{num1} {num2}'.format(num1=num1, num2=num2)
    return quest, answer
