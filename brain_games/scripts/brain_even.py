#!/usr/bin/env python3
"""Game even or not."""

from brain_games import config, game_engine
from brain_games.games import even_game


def main():
    """Start game even or not."""
    game_engine.start(
        even_game.questions_generator,
        config.INSTRUCTION_STRING_EVEN_OR_NOT_GAME,
        )


if __name__ == '__main__':
    main()
