#!/usr/bin/env python3


import prompt
from brain_games.games.brain_calc import brain_calc
from brain_games.games.brain_even import brain_even


def welcome_user():
    name = prompt.string('May I have your name? ')
    print (f'Hello, {name}!')
    return name


def main(game='brain-calc'):
    welcome_message = welcome_user()
    counter = 0
    while counter < 3:
        if game == 'brain-calc':
            question, correct_answer = brain_calc()
        elif game == 'brain-even':
            question, correct_answer = brain_even()
        else:
            print('Unknown game')
            return

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
    main(game)