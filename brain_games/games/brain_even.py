from brain_games.engine.engine import engine
from random import randint


def brain_even(welcome_message):
    print('Answer "yes" if the number is even, '
          'otherwise answer "no".')

    def generate_question():
        question = randint(1, 10)
        correct_answer = 'yes' if question % 2 == 0 else 'no'
        return question, correct_answer

    engine(welcome_message, generate_question)
