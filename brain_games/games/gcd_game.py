"""GCD game."""

from random import randint

from brain_games import config


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


def questions_generator() -> tuple:
    """Generate quest/answer for GDC game.

    Returns:
        (quest, right answer)
    """
    num1 = randint(  # noqa: S311
        config.MIN_NUMBER_FOR_GCD_GAME,
        config.MAX_NUMBER_FOR_GCD_GAME,
        )
    num2 = randint(  # noqa: S311
        config.MIN_NUMBER_FOR_GCD_GAME,
        config.MAX_NUMBER_FOR_GCD_GAME,
        )
    right_answer = str(gdc(num1, num2))
    quest = config.QUEST_GDC_STRING.format(num1=num1, num2=num2)
    return (quest, right_answer)
