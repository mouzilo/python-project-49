from random import randint
from math import gcd
from brain_games.engine.engine import engine


def brain_gcd(welcome_message):
    print('Find the greatest common divisor of given numbers.')

    def generate_question():
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        question = f'{num1} {num2}'
        correct_answer = str(gcd(num1, num2))
        return question, correct_answer

    engine(welcome_message, generate_question)
