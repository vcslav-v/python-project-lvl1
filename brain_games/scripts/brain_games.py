#!/usr/bin/env python3
"""Main script file."""

from brain_games import cli


def main():
    """Start game."""
    print('Welcome to the Brain Games!')  # noqa: WPS421
    print('Hello, {name}'.format(name=cli.welcome_user()))  # noqa: WPS421


if __name__ == '__main__':
    main()
