from brain_games.engine.engine_new import engine
from random import randint


def generate_question():
    counter2 = 0
    question = randint(1, 100)
    for i in range(2, question // 2 + 1):
        if question % i == 0:
            counter2 += 1
    correct_answer = 'yes' if counter2 <= 0 else 'no'
    return question, correct_answer


def brain_prime(welcome_message):
    engine(welcome_message, generate_question)
