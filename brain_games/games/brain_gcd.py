from random import randint
from math import gcd

START_GEN = 1
END_GEN = 10


def generate_question():
    num1 = randint(START_GEN, END_GEN)
    num2 = randint(START_GEN, END_GEN)
    question = f'{num1} {num2}'
    correct_answer = str(gcd(num1, num2))
    return question, correct_answer
