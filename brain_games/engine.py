#!/usr/bin/env python3


import prompt
from brain_games.games.brain_games import welcome_user
from brain_games.games.brain_calc import brain_calc
from brain_games.games.brain_even import brain_even


def engine(game='brain_even'):
    welcome_message = welcome_user()
    counter = 0

    while counter < 3:
        if game == 'brain_calc':
            question, correct_answer = brain_calc()
        elif game == 'brain_even':
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