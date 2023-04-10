from brain_games.engine.engine import engine
from random import randint, choice


def brain_calc(welcome_message):
    print('What is the result of the expression?')
    start_gen = 1
    end_gen = 10

    def generate_question():
        num1 = randint(start_gen, end_gen)
        num2 = randint(start_gen, end_gen)
        operation = choice(['+', '-', '*'])
        question = f'{num1} {operation} {num2}'
        correct_answer = str(eval(question))
        return question, correct_answer

    engine(welcome_message, generate_question)
