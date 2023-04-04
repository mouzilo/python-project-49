#!/usr/bin/env python3

from brain_games.games.brain_prime import brain_prime
from brain_games.scripts.brain_games import welcome_user


def prime():
    welcome_message = welcome_user()
    print('Answer "yes" if given number is prime. '
          'Otherwise answer "no".')
    brain_prime(welcome_message)


def main():
    prime()


if __name__ == '__main__':
    main()
