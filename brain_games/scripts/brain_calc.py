#!/usr/bin/env python3
"""Game Calculator - simple math quiz."""

from brain_games import engine
from brain_games.games import calc


def main():
    """Start Calculator game."""
    engine.run(calc)


if __name__ == '__main__':
    main()
