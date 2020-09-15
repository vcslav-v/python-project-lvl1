"""GCD game."""

from random import randint

from brain_games import config, game_engine


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


MIN_NUMBER = 0
MAX_NUMBER = 100
QUEST_STRING_PATTERN = '{num1} {num2}'


def get_question_answer() -> tuple:
    """Generate quest/answer for GDC game.

    Returns:
        (quest, right answer)
    """
    num1 = randint(MIN_NUMBER, MAX_NUMBER)
    num2 = randint(MIN_NUMBER, MAX_NUMBER)
    right_answer = str(gdc(num1, num2))
    question = QUEST_STRING_PATTERN.format(num1=num1, num2=num2)
    return (question, right_answer)


INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def main():
    """Start GCD game."""
    game_engine.start(
        get_question_answer,
        INSTRUCTION,
        config.RE_ANSWER_PATTERN_NUMBER,
    )


if __name__ == '__main__':
    main()
