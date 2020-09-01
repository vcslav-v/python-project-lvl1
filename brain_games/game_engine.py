"""CLI game engine."""

from brain_games import cli, config


def game(questions_generator):
    """Make common flow ask-answer-ask, return True if user win, False if not.

    Parameters:
        questions_generator: function return ('quest','right_answer')

    Returns:
        bool
    """
    attempt = 0
    while attempt < config.NUMBER_OF_ATTEMPTS:
        quest, right_answer = questions_generator()
        cli.text_to_out(config.QUESTION_STRING.format(quest=quest))
        is_win, answer = check_win(right_answer)
        if not is_win:
            break
        cli.text_to_out(config.CORRECT_STRING, big_gap=True)
        attempt += 1
    else:
        return True
    cli.text_to_out(config.WRONG_STRING.format(
        wrong_answer=answer,
        right_answer=right_answer,
        ))
    return False


def check_win(right_answer):
    """Ask player's answer, return True if player win or False if lose.

    Parameters:
        right_answer: str

    Returns:
        (bool, str)
    """
    answer = cli.ask_user()
    if answer == right_answer:
        return True, answer
    return False, answer


def summary(name, player_result):
    """Print sums up the game.

    Parameters:
        name: str
        player_result: bool
    """
    if player_result:
        cli.text_to_out(config.WIN_STRING.format(name=name), big_gap=True)
    else:
        cli.text_to_out(config.LOSE_STRING.format(name=name), big_gap=True)


def start(questions_generator, instuction):
    """Start game flow.

    Parameters:
        questions_generator: function return ('quest','right_answer')
        instuction: str
    """
    cli.welcome(instuction)
    name = cli.ask_name()
    player_result = game(questions_generator)
    summary(name, player_result)
