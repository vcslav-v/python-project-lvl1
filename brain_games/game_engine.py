"""CLI game engine."""

from brain_games import cli, config


def game(questions_generator) -> bool:
    """Make common flow ask-answer-ask.

    Parameters:
        questions_generator: function return ('quest','right_answer')

    Returns:
        True if user win, False if not
    """
    attempt = 0
    while attempt < config.NUMBER_OF_ATTEMPTS:
        quest, right_answer = questions_generator()
        cli.text_to_out(config.QUESTION_STRING.format(quest=quest))
        answer = cli.ask_user()
        if answer != right_answer:
            cli.text_to_out(config.WRONG_STRING.format(
                wrong_answer=answer,
                right_answer=right_answer,
                ))
            return False
        cli.text_to_out(config.CORRECT_STRING, big_gap=True)
        attempt += 1
    return True


def summary(name: str, player_result: bool):
    """Print sums up the game.

    Parameters:
        name: Name of player
        player_result: True if player win, False if one lose
    """
    if player_result:
        cli.text_to_out(config.WIN_STRING.format(name=name), big_gap=True)
    else:
        cli.text_to_out(config.LOSE_STRING.format(name=name), big_gap=True)


def start(questions_generator, instuction: str):
    """Start game flow.

    Parameters:
        questions_generator: function return ('quest','right_answer')
        instuction: String instruction for game
    """
    cli.welcome(instuction)
    name = cli.ask_name()
    player_result = game(questions_generator)
    summary(name, player_result)
