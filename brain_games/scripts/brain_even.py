from brain_games.games.brain_even import brain_even
from brain_games.engine.engine_new import engine
from brain_games.games.brain_games import welcome_user


def even():
    welcome_message = welcome_user()
    print(f'Answer "yes" if the number is even, '
          f'otherwise answer "no".')
    question, correct_answer = brain_even()
    engine(welcome_message, question, correct_answer)


def main():
    even()


'''
    comment_map = {
        'brain_gcd': 'Find the greatest common divisor of given numbers.',
        'brain_progression': 'What number is missing in the progression?',
        'brain_prime': 'Answer "yes" if given number is prime. '
                       'Otherwise answer "no".'
    }
'''
if __name__ == '__main__':
    main()