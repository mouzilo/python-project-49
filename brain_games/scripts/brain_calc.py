#!/usr/bin/env python3

from brain_games.engine.engine import engine
from brain_games.games.brain_calc import generate_question


def main():
    message = 'What is the result of the expression?'
    engine(message, generate_question)


if __name__ == '__main__':
    main()
