"""Command Line Interface tools."""

import prompt

from brain_games import config


def welcome_user() -> str:
    """
    Asks the user for their name'.

    Returns:
        Player name
    """
    return prompt.string('May I have your name? ')


def welcome(instuction: str):
    """Greets the player.

    Parameters:
        instuction: String-instruction for the game
    """
    text_to_out(config.HELLO_STRING)
    text_to_out(instuction, big_gap=True)


def ask_name() -> str:
    """Asks for the player's name.

    Returns:
        Player name
    """
    name = prompt.string(config.ASK_NAME_STRING)
    text_to_out(config.HELLO_NAME_STRING.format(name=name), big_gap=True)
    return name


def ask_user(pattern: str = '.*') -> str:
    """Ask user answer and return.

    Parameters:
        pattern: regex pattern for check correctly user answer

    Returns:
        Player's answer
    """
    answer = prompt.regex(pattern, prompt=config.ASK_ANSWER_STRING)
    return answer.group()


def text_to_out(text: str, big_gap: bool = False):
    """Print text to std.out.

    Parameters:
        text: What must be print
        big_gap: Do need to use increased indentation after a line
    """
    if big_gap:
        print(text, end=config.GAP_STING)  # noqa:WPS421
    else:
        print(text)  # noqa:WPS421
