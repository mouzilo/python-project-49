#!/usr/bin/env python3

from brain_games.games.brain_gcd import generate_question
from brain_games.engine.engine import engine


def main():
    message = 'Find the greatest common divisor of given numbers.'
    engine(message, generate_question)


if __name__ == '__main__':
    main()
