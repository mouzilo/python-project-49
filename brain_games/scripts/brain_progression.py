#!/usr/bin/env python3

from brain_games.games.brain_progression import generate_question
from brain_games.engine.engine import engine, welcome_user


def main():
    welcome_message = welcome_user()
    print('What number is missing in the progression?')
    engine(welcome_message, generate_question)


if __name__ == '__main__':
    main()
