from brain_games.engine.engine import engine
from random import randint, choice


def brain_calc(welcome_message):
    print('What is the result of the expression?')

    def generate_question():
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        operation = choice(['+', '-', '*'])
        question = f'{num1} {operation} {num2}'
        correct_answer = str(eval(question))
        return question, correct_answer

    engine(welcome_message, generate_question)
