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
        print('What is the result of the expression?')
    elif game == 'brain_even':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif game == 'brain_gcd':
        print('Find the greatest common divisor of given numbers.')
    elif game == 'brain_progression':
        print('What number is missing in the progression?')
    elif game == 'brain_prime':
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
    else:
        print('Unknown game')

    game_map = {
        'brain_calc': brain_calc,
        'brain_even': brain_even,
        'brain_gcd': brain_gcd,
        'brain_progression': brain_progression,
        'brain_prime': brain_prime,
    }

    if game not in game_map:
        print('Unknown game')
        return

    while counter < 3:
        question, correct_answer = game_map[game]()
        print('Question:', question)
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. \n"
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {welcome_message}!")
            return

    print(f'Congratulations, {welcome_message}!')
