from random import randint

START_GEN = 1
END_GEN = 10


def generate_question():
    question = randint(START_GEN, END_GEN)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return question, correct_answer
