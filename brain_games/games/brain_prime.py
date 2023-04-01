import prompt
from brain_games.engine.engine_new import engine
from random import randint


def brain_prime(welcome_message):
    counter = 1
    while counter <= 3:
        counter2 = 0
        question = randint(1, 100)
        for i in range(2, question // 2 + 1):
            if question % i == 0:
                counter2 += 1
        correct_answer = 'yes' if counter2 <= 0 else 'no'
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        result = engine(welcome_message, correct_answer, answer, counter)
        if result == "Correct!":
            print(result)
            counter += 1
        else:
            return result
    print(engine(welcome_message, "", "", 3))
