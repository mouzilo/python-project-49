from brain_games.games.brain_gcd import brain_gcd
from brain_games.engine.engine_new import engine
from brain_games.games.brain_games import welcome_user


def gcd():
    welcome_message = welcome_user()
    print(f'Find the greatest common divisor of given numbers.')
    question, correct_answer = brain_gcd()
    engine(welcome_message, question, correct_answer)


def main():
    gcd()


'''
    comment_map = {
        'brain_progression': 'What number is missing in the progression?',
        'brain_prime': 'Answer "yes" if given number is prime. '
                       'Otherwise answer "no".'
    }
'''
if __name__ == '__main__':
    main()