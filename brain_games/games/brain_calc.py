from brain_games.engine.engine_new import engine
from random import randint, choice


def generate_question():
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    operation = choice(['+', '-', '*'])
    question = f'{num1} {operation} {num2}'
    correct_answer = str(eval(question))
    return question, correct_answer


def brain_calc(welcome_message):
    engine(welcome_message, generate_question)
