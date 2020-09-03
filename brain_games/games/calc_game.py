"""Calculator game."""

from operator import add, mul, sub
from random import choice, randint

from brain_games import config


def questions_generator() -> tuple:
    """Generate quest/answer for Calculator game.

    Returns:
        (quest, right answer)
    """
    num1 = randint(  # noqa: S311
        config.MIN_NUMBER_FOR_CALCULATOR_GAME,
        config.MAX_NUMBER_FOR_CALCULATOR_GAME,
        )
    num2 = randint(  # noqa: S311
        config.MIN_NUMBER_FOR_CALCULATOR_GAME,
        config.MAX_NUMBER_FOR_CALCULATOR_GAME,
        )
    operations = {
        '+': add(num1, num2),
        '-': sub(num1, num2),
        '*': mul(num1, num2),
    }
    operation = choice(list(operations))  # noqa: S311
    expression = config.QUEST_EVAL_STRING.format(
        num1=str(num1),
        operation=operation,
        num2=str(num2),
        )
    return (expression, str(operations[operation]))
