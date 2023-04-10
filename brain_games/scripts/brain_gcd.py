#!/usr/bin/env python3

from brain_games.games.brain_gcd import brain_gcd
from brain_games.scripts.brain_games import welcome_user


def main():
    welcome_message = welcome_user()
    brain_gcd(welcome_message)


if __name__ == '__main__':
    main()
