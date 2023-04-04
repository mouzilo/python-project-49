#!/usr/bin/env python3

from brain_games.games.brain_calc import brain_calc
from brain_games.scripts.brain_games import welcome_user


def calc():
    welcome_message = welcome_user()
    print('What is the result of the expression?')
    brain_calc(welcome_message)


def main():
    calc()


if __name__ == '__main__':
    main()
