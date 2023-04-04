from random import randint
from math import gcd
from brain_games.engine.engine_new import engine


def generate_question():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = f'{num1} {num2}'
    correct_answer = str(gcd(num1, num2))
    return question, correct_answer


def brain_gcd(welcome_message):
    engine(welcome_message, generate_question)
