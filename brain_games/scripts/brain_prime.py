#!/usr/bin/env python3

from brain_games.games.brain_prime import brain_prime
from brain_games.scripts.brain_games import welcome_user


def main():
    welcome_message = welcome_user()
    brain_prime(welcome_message)


if __name__ == '__main__':
    main()
