from random import randint, choice


def brain_calc():
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    operation = choice(['+', '-', '*'])
    question = f'{num1} {operation} {num2}'
    correct_answer = str(eval(question))
    return question, correct_answer
