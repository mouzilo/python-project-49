#!/usr/bin/env python3


import prompt
from random import randint, choice
from games.brain_calc import brain_calc
from games.brain_even import brain_even


def welcome_user():
    name = prompt.string('May I have your name? ')
    print (f'Hello, {name}!')
    return name


def run_game(game):
    welcome_message = welcome_user()
    counter = 0
    while counter < 3:
        question, correct_answer = game()
        print('Question:', question)
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {welcome_message}!")
            return
    print(f'Congratulations, {welcome_message}!')



if __name__ == '__main__':
    run_game(game)
