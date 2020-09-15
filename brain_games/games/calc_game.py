"""Calculator game."""

from operator import add, mul, sub
from random import choice, randint

from brain_games import config, game_engine

MIN_NUMBER = 0
MAX_NUMBER = 20
QUEST_EVAL_STRING = '{num1} {operation} {num2}'


def get_question_answer() -> tuple:
    """Generate quest/answer for Calculator game.

    Returns:
        (quest, right answer)
    """
    num1 = randint(MIN_NUMBER, MAX_NUMBER)
    num2 = randint(MIN_NUMBER, MAX_NUMBER)
    operations = {
        '+': add,
        '-': sub,
        '*': mul,
    }
    operation = choice(list(operations))
    expression = QUEST_EVAL_STRING.format(
        num1=str(num1),
        operation=operation,
        num2=str(num2),
    )
    return (expression, str(operations[operation](num1, num2)))


INSTRUCTION = 'What is the result of the expression?'


def main():
    """Start calculator game."""
    game_engine.start(
        get_question_answer,
        INSTRUCTION,
        config.RE_ANSWER_PATTERN_NUMBER,
    )


if __name__ == '__main__':
    main()
