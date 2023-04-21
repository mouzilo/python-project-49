#!/usr/bin/env python3

from brain_games.engine.engine import engine
from brain_games.games.brain_even import generate_question


def main():
    message = 'Answer "yes" if the number is even, \nOtherwise answer "no".'
    engine(message, generate_question)


if __name__ == '__main__':
    main()
