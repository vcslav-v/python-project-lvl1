"""Command Line Interface tools."""

import prompt

from brain_games import config


def welcome_user():
    """
    Asks the user for their name'.

    Returns:
        str
    """
    return prompt.string('May I have your name? ')


def welcome(instuction):
    """Greets the player.

    Parameters:
        instuction: str
    """
    text_to_out(config.HELLO_STRING)
    text_to_out(instuction, big_gap=True)


def ask_name():
    """Asks for the player's name.

    Returns:
        str
    """
    name = prompt.string(config.ASK_NAME_STRING)
    text_to_out(config.HELLO_NAME_STRING.format(name=name), big_gap=True)
    return name


def ask_user():
    """Ask user answer and return.

    Returns:
        str
    """
    return prompt.string(config.ASK_ANSWER_STRING)


def text_to_out(text, big_gap=False):
    """Print text to std.out.

    Parameters:
        text:str
        big_gap:bool
    """
    if big_gap:
        print(text, end=config.GAP_STING)  # noqa:WPS421
    else:
        print(text)  # noqa:WPS421
