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

    print(game_map[game].__doc__)

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
