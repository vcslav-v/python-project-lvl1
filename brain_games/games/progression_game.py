"""Progression game."""

from random import randint

from brain_games import config, game_engine

LENGTH_OF_PROGRESSION = 10


def make_progression(start_num: int, difference: int) -> list:
    """Generate arithmetic progression.

    Parameters:
        start_num: First progression's element
        difference: Difference betwin n+1 and n progression's elements

    Returns:
        Progression
    """
    progression = []
    for multiplier in range(LENGTH_OF_PROGRESSION):
        progression.append(start_num + difference * multiplier)
    return progression


MIN_DIFF = 1
MAX_DIFF = 10
MIN_START = 0
MAX_START = 10
SEPARATOR = ' '
LOSE_ELEMENT = '..'


def get_question_answer() -> tuple:
    """Generate quest/answer for Progression game.

    Returns:
        (quest, right answer)
    """
    difference = randint(MIN_DIFF, MAX_DIFF)
    start_num = randint(MIN_START, MAX_START)
    progression = make_progression(start_num, difference)

    question_index = randint(0, LENGTH_OF_PROGRESSION - 1)
    question = start_num + difference * question_index

    progression = list(map(str, progression))
    progression[question_index] = LOSE_ELEMENT

    return SEPARATOR.join(progression), str(question)


INSTRUCTION = 'What number is missing in the progression?'


def main():
    """Start progression game."""
    game_engine.start(
        get_question_answer,
        INSTRUCTION,
        config.RE_ANSWER_PATTERN_NUMBER,
    )


if __name__ == '__main__':
    main()
