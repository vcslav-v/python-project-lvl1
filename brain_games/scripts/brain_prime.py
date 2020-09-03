#!/usr/bin/env python3
"""Game prime."""

from brain_games import config, game_engine
from brain_games.games import prime_game


def main():
    """Start prime game."""
    game_engine.start(
        prime_game.questions_generator,
        config.INSTRUCTION_STRING_PRIME_GAME,
        config.RE_ANSWER_PATTERN_YES_OR_NO,
        )


if __name__ == '__main__':
    main()
