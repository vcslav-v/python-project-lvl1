#!/usr/bin/env python3
"""Game Calculator - simple math quiz."""

from brain_games import config, game_engine
from brain_games.games import calc_game


def main():
    """Start Calculator game."""
    game_engine.start(
        calc_game.questions_generator,
        config.INSTRUCTION_STRING_CALC_GAME,
        config.RE_ANSWER_PATTERN_NUMBER,
        )


if __name__ == '__main__':
    main()
