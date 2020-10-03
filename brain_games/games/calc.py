"""Calculator game."""

from operator import add, mul, sub
from random import choice, randint

MIN_NUMBER = 0
MAX_NUMBER = 20
QUEST_EVAL_STRING = '{num1} {operation} {num2}'
INSTRUCTION = 'What is the result of the expression?'


def get_round_data() -> tuple:
    """Generate quest/answer for Calculator game.

    Returns:
        (quest, right answer)
    """
    num1 = randint(MIN_NUMBER, MAX_NUMBER)
    num2 = randint(MIN_NUMBER, MAX_NUMBER)
    operations = [
        ('+', add),
        ('-', sub),
        ('*', mul),
    ]
    operation, execute = choice(operations)
    quest = QUEST_EVAL_STRING.format(
        num1=str(num1),
        operation=operation,
        num2=str(num2),
    )
    answer = str(execute(num1, num2))
    return quest, answer
