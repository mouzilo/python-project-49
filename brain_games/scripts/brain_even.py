#!/usr/bin/env python3

from brain_games.engine.engine import engine, welcome_user
from brain_games.games.brain_even import generate_question


def main():
    welcome_message = welcome_user()
    print('Answer "yes" if the number is even, '
          'otherwise answer "no".')
    engine(welcome_message, generate_question)


if __name__ == '__main__':
    main()
