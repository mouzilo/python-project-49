from random import randint, choice
import prompt
from brain_games.engine.engine_new import engine


def brain_calc(welcome_message):
    counter = 1
    while counter <= 3:
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        operation = choice(['+', '-', '*'])
        question = f'{num1} {operation} {num2}'
        correct_answer = str(eval(question))
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        result = engine(welcome_message, correct_answer, answer, counter)
        if result == "Correct!":
            print(result)
            counter += 1
        else:
            return result
    print(engine(welcome_message, "", "", 3))
