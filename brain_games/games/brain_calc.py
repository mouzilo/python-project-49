#!/usr/bin/env python3


from random import randint, choice


def brain_calc():
    # print(f'What is the result of the expression?')
    counter = 0
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    operation = choice(['+', '-', '*'])
    question = f'{num1} {operation} {num2}'
    correct_answer = str(eval(question))
    return question, correct_answer