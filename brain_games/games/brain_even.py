from brain_games.engine.engine import engine
from random import randint


def brain_even(welcome_message):
    print('Answer "yes" if the number is even, '
          'otherwise answer "no".')
    start_gen = 1
    end_gen = 10

    def generate_question():
        question = randint(start_gen, end_gen)
        correct_answer = 'yes' if question % 2 == 0 else 'no'
        return question, correct_answer

    engine(welcome_message, generate_question)
