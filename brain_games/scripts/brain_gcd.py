#!/usr/bin/env python3

from brain_games.games.brain_gcd import brain_gcd
from brain_games.scripts.brain_games import welcome_user


def gcd():
    welcome_message = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    brain_gcd(welcome_message)


def main():
    gcd()


if __name__ == '__main__':
    main()
