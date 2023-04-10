from brain_games.engine.engine import engine
from random import randint


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def brain_prime(welcome_message):
    print('Answer "yes" if given number is prime. '
          'Otherwise answer "no".')
    start_gen = 1
    end_gen = 10

    def generate_question():
        question = randint(start_gen, end_gen)
        correct_answer = 'yes' if is_prime(question) else 'no'
        return question, correct_answer
    engine(welcome_message, generate_question)
