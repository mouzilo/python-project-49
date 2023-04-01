from brain_games.games.brain_progression import brain_progression
from brain_games.engine.engine_new import engine
from brain_games.games.brain_games import welcome_user


def progression():
    welcome_message = welcome_user()
    print(f'What number is missing in the progression?')
    question, correct_answer = brain_progression()
    engine(welcome_message, question, correct_answer)


def main():
    progression()


'''
    comment_map = {
        'brain_prime': 'Answer "yes" if given number is prime. '
                       'Otherwise answer "no".'
    }
'''
if __name__ == '__main__':
    main()