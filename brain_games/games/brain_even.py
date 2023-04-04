from brain_games.engine.engine_new import engine
from random import randint


def generate_question():
    question = randint(1, 10)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return question, correct_answer


def brain_even(welcome_message):
    engine(welcome_message, generate_question)
