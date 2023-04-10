from random import randint
from math import gcd
from brain_games.engine.engine import engine


def brain_gcd(welcome_message):
    print('Find the greatest common divisor of given numbers.')
    start_gen = 1
    end_gen = 10

    def generate_question():
        num1 = randint(start_gen, end_gen)
        num2 = randint(start_gen, end_gen)
        question = f'{num1} {num2}'
        correct_answer = str(gcd(num1, num2))
        return question, correct_answer

    engine(welcome_message, generate_question)
