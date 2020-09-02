"""Progression game."""

from random import choice, randint

from brain_games import config


def make_progression(start_num, difference):
    """Generate arithmetic progression.

    Parameters:
        start_num:int
        difference:int

    Returns:
        list
    """
    progression = []
    for multiplier in range(config.LENGTH_OF_PROGRESSION):
        progression.append(start_num + difference * multiplier)
    return progression


def quest_progression(progression):
    """Generate quest progression with lose element from list.

    Parameters:
        progression:list

    Returns:
        tuple
    """
    quest_num = choice(progression)  # noqa:S311
    str_pogression = ''
    for element in progression:
        if element == quest_num:
            str_pogression += (
                config.ELEMENT_OF_PROGRESSION.format(
                    element=config.LOSE_ELEMENT,
                    )
            )
        else:
            str_pogression += (
                config.ELEMENT_OF_PROGRESSION.format(element=str(element))
            )
    return str_pogression.strip(), str(quest_num)


def questions_generator():
    """Generate quest/answer for Progression game.

    Returns:
        tuple
    """
    difference = randint(  # noqa: S311
        config.MIN_DIFF_FOR_PROGRESSION_GAME,
        config.MAX_DIFF_FOR_PROGRESSION_GAME,
        )
    start_num = randint(  # noqa: S311
        config.MIN_START_FOR_PROGRESSION_GAME,
        config.MAX_START_FOR_PROGRESSION_GAME,
        )
    progression = make_progression(start_num, difference)
    return quest_progression(progression)
