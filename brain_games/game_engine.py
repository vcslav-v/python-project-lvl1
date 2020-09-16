"""CLI game engine."""

from brain_games import cli, config


def game(questions_generator, answer_re_pattern) -> bool:
    """Make common flow ask-answer-ask.

    Parameters:
        questions_generator: function return ('quest','right_answer')
        answer_re_pattern: regex pattern for check correctly user answer

    Returns:
        True if user win, False if not
    """
    attempt = 0
    while attempt < config.NUMBER_OF_ATTEMPTS:
        quest, right_answer = questions_generator()
        cli.text_to_out(config.QUESTION_STRING.format(quest=quest))
        answer = cli.ask_user(pattern=answer_re_pattern)
        if answer != right_answer:
            cli.text_to_out(config.WRONG_STRING.format(
                wrong_answer=answer,
                right_answer=right_answer,
            ))
            return False
        cli.text_to_out(config.CORRECT_STRING, big_gap=True)
        attempt += 1
    return True


def start(
    questions_generator: callable,
    instuction: str,
    answer_re_pattern: str = '.*',
):
    """Start game flow.

    Parameters:
        questions_generator: function return ('quest','right_answer')
        instuction: String instruction for game
        answer_re_pattern: regex pattern for check correctly user answer
    """
    cli.text_to_out(config.HELLO_STRING)
    cli.text_to_out(instuction, big_gap=True)

    name = cli.ask_user(text=config.ASK_NAME_STRING)
    cli.text_to_out(config.HELLO_NAME_STRING.format(name=name), big_gap=True)

    player_result = game(questions_generator, answer_re_pattern)
    if player_result:
        cli.text_to_out(config.WIN_STRING.format(name=name), big_gap=True)
    else:
        cli.text_to_out(config.LOSE_STRING.format(name=name), big_gap=True)
