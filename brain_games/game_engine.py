"""CLI game engine."""

from brain_games import cli, config


def start(
    questions_generator: callable,
    instuction: str,
):
    """Start game flow.

    Parameters:
        questions_generator: function return ('quest','right_answer')
        instuction: String instruction for game
    """
    cli.text_to_out(config.HELLO_STRING)
    cli.text_to_out(instuction, big_gap=True)

    name = cli.ask_user(text=config.ASK_NAME_STRING)
    cli.text_to_out(config.HELLO_NAME_STRING.format(name=name), big_gap=True)

    attempt = 0
    while attempt < config.NUMBER_OF_ATTEMPTS:
        quest, right_answer = questions_generator()
        cli.text_to_out(config.QUESTION_STRING.format(quest=quest))
        if isinstance(right_answer, int):
            answer = cli.ask_user(pattern=config.RE_ANSWER_PATTERN_NUMBER)
        else:
            answer = cli.ask_user(pattern=config.RE_ANSWER_PATTERN_YES_OR_NO)

        if answer != str(right_answer):
            cli.text_to_out(config.WRONG_STRING.format(
                wrong_answer=answer,
                right_answer=right_answer,
            ))
            cli.text_to_out(config.LOSE_STRING.format(name=name), big_gap=True)
            break

        cli.text_to_out(config.CORRECT_STRING, big_gap=True)
        attempt += 1
    else:
        cli.text_to_out(config.WIN_STRING.format(name=name), big_gap=True)
