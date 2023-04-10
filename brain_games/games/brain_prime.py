from brain_games.engine.engine import engine
from random import randint


def brain_prime(welcome_message):
    print('Answer "yes" if given number is prime. '
          'Otherwise answer "no".')

    def generate_question():
        counter2 = 0
        question = randint(1, 100)
        for i in range(2, question // 2 + 1):
            if question % i == 0:
                counter2 += 1
        correct_answer = 'yes' if counter2 <= 0 else 'no'
        return question, correct_answer
    engine(welcome_message, generate_question)
