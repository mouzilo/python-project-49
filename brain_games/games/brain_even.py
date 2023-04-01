from brain_games.engine.engine_new import engine
from random import randint
import prompt


def brain_even(welcome_message):
    # print(f'Answer "yes" if the number is even, otherwise answer "no".')
    counter = 1
    while counter <= 3:
        question = randint(1, 10)
        correct_answer = 'yes' if question % 2 == 0 else 'no'
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        result = engine(welcome_message, correct_answer, answer, counter)
        if result == "Correct!":
            print(result)
            counter += 1
        else:
            return result
    print(engine(welcome_message, "", "", 3))
