"""Prime game."""

from math import sqrt
from random import randint

from brain_games import config, game_engine


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


MIN_NUMBER = 1
MAX_NUMBER = 1000


def get_question_answer() -> tuple:
    """Generate quest/answer for Prime game.

    Returns:
        (quest, right answer)
    """
    number = randint(MIN_NUMBER, MAX_NUMBER)
    if is_prime(number):
        answer = config.YES_ANSWER
    else:
        answer = config.NO_ANSWER
    return str(number), answer


INSTRUCTION = (
    'Answer "{yes}" if given number is prime. Otherwise answer "{no}".'
).format(yes=config.YES_ANSWER, no=config.NO_ANSWER)


def main():
    """Start prime game."""
    game_engine.start(
        get_question_answer,
        INSTRUCTION,
        config.RE_ANSWER_PATTERN_YES_OR_NO,
    )


if __name__ == '__main__':
    main()
