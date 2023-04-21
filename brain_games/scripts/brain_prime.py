#!/usr/bin/env python3

from brain_games.games.brain_prime import generate_question
from brain_games.engine.engine import engine, welcome_user


def main():
    welcome_message = welcome_user()
    print('Answer "yes" if given number is prime. '
          'Otherwise answer "no".')
    engine(welcome_message, generate_question)


if __name__ == '__main__':
    main()
