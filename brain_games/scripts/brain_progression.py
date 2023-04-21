#!/usr/bin/env python3

from brain_games.games.brain_progression import generate_question
from brain_games.engine.engine import engine


def main():
    message = 'What number is missing in the progression?'
    engine(message, generate_question)


if __name__ == '__main__':
    main()
