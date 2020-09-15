"""Even or not game."""

from random import randint

from brain_games import config, game_engine

MIN_NUMBER = -100
MAX_NUMBER = 100


def get_question_answer() -> tuple:
    """Generate quest/answer for even or not game.

    Returns:
        (quest, right answer)
    """
    question = randint(MIN_NUMBER, MAX_NUMBER)
    if question % 2 == 0:
        right_answer = config.YES_ANSWER
    else:
        right_answer = config.NO_ANSWER
    return (question, right_answer)


INSTRUCTION = (
    'Answer "{yes}" if number even otherwise answer "{no}".'
).format(yes=config.YES_ANSWER, no=config.NO_ANSWER)


def main():
    """Start Even or not game."""
    game_engine.start(
        get_question_answer,
        INSTRUCTION,
        config.RE_ANSWER_PATTERN_YES_OR_NO,
    )


if __name__ == '__main__':
    main()
