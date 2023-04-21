from random import randint, choice

START_GEN = 1
END_GEN = 10


def generate_question():
    num1 = randint(START_GEN, END_GEN)
    num2 = randint(START_GEN, END_GEN)
    operation = choice(['+', '-', '*'])
    question = f'{num1} {operation} {num2}'
    correct_answer = str(eval(question))
    return question, correct_answer
