"""Even or not game."""

from random import randint

from brain_games import config


def questions_generator():
    """Generate quest/answer for even or not game.

    Returns:
        tuple
    """
    quest = randint(  # noqa: S311
        config.MIN_NUMBER_FOR_QUESTION_EVEN_OR_NOT_GAME,
        config.MAX_NUMBER_FOR_QUESTION_EVEN_OR_NOT_GAME,
        )
    if quest % 2 == 0:
        right_answer = config.YES_ANSWER
    else:
        right_answer = config.NO_ANSWER
    return (quest, right_answer)
