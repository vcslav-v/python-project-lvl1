"""Command Line Interface tools."""

import prompt


def welcome_user():
    """
    Asks the user for their name'.

    Returns:
        str
    """
    return prompt.string('May I have your name? ')
