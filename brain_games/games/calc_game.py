"""Calculator game."""

from random import choice, randint

from brain_games import config


def solver(num1, num2, operation):
    """Solve expression like num1 {operation} num2, {operation} can be '+'/'-'/'*'.

    Parameters:
        num1:int
        num2:int
        operation:str

    Returns:
        str
    """
    if operation == config.PLUS:
        return str(num1 + num2)
    elif operation == config.MINUS:
        return str(num1 - num2)
    elif operation == config.MULTIPLY:
        return str(num1 * num2)
    return config.ERROR_STRING


def questions_generator():
    """Generate quest/answer for Calculator game.

    Returns:
        tuple
    """
    num1 = randint(  # noqa: S311
        config.MIN_NUMBER_FOR_CALCULATOR_GAME,
        config.MAX_NUMBER_FOR_CALCULATOR_GAME,
        )
    num2 = randint(  # noqa: S311
        config.MIN_NUMBER_FOR_CALCULATOR_GAME,
        config.MAX_NUMBER_FOR_CALCULATOR_GAME,
        )
    operation = choice(config.OPERATIONS)  # noqa: S311
    expression = config.QUEST_EVAL_STRING.format(
        num1=str(num1),
        operation=operation,
        num2=str(num2),
        )
    right_answer = solver(num1, num2, operation)
    return (expression, right_answer)
