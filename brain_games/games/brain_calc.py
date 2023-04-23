from random import randint, choice

START_GEN = 1
END_GEN = 10


def print_description():
    print('What is the result of the expression?')


def generate_question():
    num1 = randint(START_GEN, END_GEN)
    num2 = randint(START_GEN, END_GEN)
    operation = choice(['+', '-', '*'])
    question = f'{num1} {operation} {num2}'
    if operation == '+':
        correct_answer = str(num1 + num2)
    elif operation == '-':
        correct_answer = str(num1 - num2)
    else:
        correct_answer = str(num1 * num2)
    return question, correct_answer
