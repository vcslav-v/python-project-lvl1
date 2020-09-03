#!/usr/bin/env python3
"""Game Progression - find lose element in progression."""

from brain_games import config, game_engine
from brain_games.games import progression_game


def main():
    """Start Progression game."""
    game_engine.start(
        progression_game.questions_generator,
        config.INSTRUCTION_STRING_PROGRESSION_GAME,
        config.RE_ANSWER_PATTERN_NUMBER,
        )


if __name__ == '__main__':
    main()
