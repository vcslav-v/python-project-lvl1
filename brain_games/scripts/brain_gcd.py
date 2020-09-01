#!/usr/bin/env python3
"""Game GCD - find greatest common divisor."""

from brain_games import config, game_engine
from brain_games.games import gcd_game


def main():
    """Start GCD game."""
    game_engine.start(
        gcd_game.questions_generator,
        config.INSTRUCTION_STRING_GCD_GAME,
        )


if __name__ == '__main__':
    main()
