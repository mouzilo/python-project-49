from random import randint, choice

START_GEN = 1
END_GEN = 10
DESCRIPTION = 'What is the result of the expression?'


def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ValueError('division by zero')
        return num1 / num2


def generate_question():
    num1 = randint(START_GEN, END_GEN)
    num2 = randint(START_GEN, END_GEN)
    operation = choice(['+', '-', '*'])
    question = f'{num1} {operation} {num2}'
    correct_answer = str(calculate(num1, num2, operation))
    return question, correct_answer
