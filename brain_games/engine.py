"""CLI game engine."""
import re

from brain_games import cli, config


def run(game):
    """Run game flow.

    Parameters:
        game: object with function  get_round_data -> (quest, answer)
            and 'INSTRUCTION' for game.
    """
    cli.print_text(config.HELLO_PATTERN)
    cli.print_text(game.INSTRUCTION, big_gap=True)

    name = cli.ask(text=config.NAME_PATTERN)
    cli.print_text(config.HELLO_NAME_PATTERN.format(name=name), big_gap=True)

    attempt = 0
    while attempt < config.NUMBER_OF_ATTEMPTS:
        quest, right_answer = game.get_round_data()
        cli.print_text(config.QUESTION_PATTERN.format(quest=quest))
        answer = ask_user(right_answer)

        if answer != right_answer:
            cli.print_text(config.WRONG_PATTERN.format(
                wrong_answer=answer,
                right_answer=right_answer,
            ))
            cli.print_text(config.LOSE_PATTERN.format(name=name), big_gap=True)
            break

        cli.print_text(config.CORRECT_PATTERN, big_gap=True)
        attempt += 1
    else:
        cli.print_text(config.WIN_PATTERN.format(name=name), big_gap=True)


def ask_user(right_answer: str) -> str:
    """Ask user answer. It can be: number answer, yes/no answer or else.

    Parameters:
        right_answer: expect answer

    Returns:
        User answer
    """
    if re.search(config.RE_ANSWER_PATTERN_NUMBER, right_answer):
        return cli.ask(pattern=config.RE_ANSWER_PATTERN_NUMBER)

    elif re.search(config.RE_ANSWER_PATTERN_YES_OR_NO, right_answer):
        return cli.ask(pattern=config.RE_ANSWER_PATTERN_YES_OR_NO)

    return cli.ask()
