"""Calculator game."""

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
    operation = choice(list(config.OPERATIONS))  # noqa: S311
    expression = config.QUEST_EVAL_STRING.format(
        num1=str(num1),
        operation=operation,
        num2=str(num2),
        )
    right_answer = str(config.OPERATIONS[operation](num1, num2))
    return (expression, right_answer)
