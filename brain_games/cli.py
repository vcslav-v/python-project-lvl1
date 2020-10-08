"""Command Line Interface tools."""

import prompt

from brain_games import config


def ask(
    text: str = config.ANSWER_PATTERN,
    pattern: str = '.*',
) -> str:
    """Ask answer and return.

    Parameters:
        pattern: regex pattern for check correctly user answer
        text: question text

    Returns:
        Player's answer
    """
    answer = prompt.regex(pattern, prompt=text)
    return answer.group()


def print_text(text: str, big_gap: bool = False):
    """Print text to steam.

    Parameters:
        text: What must be print
        big_gap: Do need to use increased indentation after a line
    """
    if big_gap:
        print(text, end=config.GAP_STING)  # noqa:WPS421
    else:
        print(text)  # noqa:WPS421
