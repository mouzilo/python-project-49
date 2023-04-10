#!/usr/bin/env python3

from brain_games.games.brain_even import brain_even
from brain_games.scripts.brain_games import welcome_user


def main():
    welcome_message = welcome_user()
    brain_even(welcome_message)


if __name__ == '__main__':
    main()
