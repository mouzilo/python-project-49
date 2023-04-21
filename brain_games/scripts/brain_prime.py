#!/usr/bin/env python3

from brain_games.games.brain_prime import generate_question
from brain_games.engine.engine import engine


def main():
    message = 'Answer "yes" if given number is prime, \notherwise answer "no".'
    engine(message, generate_question)


if __name__ == '__main__':
    main()
