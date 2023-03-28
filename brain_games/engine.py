#!/usr/bin/env python3


import prompt
from brain_games.games.brain_games import welcome_user
from brain_games.games.brain_calc import brain_calc
from brain_games.games.brain_even import brain_even
from brain_games.games.brain_gcd import brain_gcd
from brain_games.games.brain_progression import brain_progression
from brain_games.games.brain_prime import brain_prime


def engine(game='brain_even'):
    welcome_message = welcome_user()
    counter = 0
    if game == 'brain_calc':
        print(f'What is the result of the expression?')
    elif game == 'brain_even':
        print(f'Answer "yes" if the number is even, otherwise answer "no".')
    elif game == 'brain_gcd':
        print(f'Find the greatest common divisor of given numbers.')
    elif game == 'brain_progression':
        print(f'What number is missing in the progression?')
    elif game == 'brain_prime':
        print(f'Answer "yes" if given number is prime. Otherwise answer "no".')
    else:
        print('Unknown game')
    while counter < 3:
        if game == 'brain_calc':
            question, correct_answer = brain_calc()
        elif game == 'brain_even':
            question, correct_answer = brain_even()
        elif game == 'brain_gcd':
            question, correct_answer = brain_gcd()
        elif game == 'brain_progression':
            question, correct_answer = brain_progression()
        elif game == 'brain_prime':
            question, correct_answer = brain_prime()
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