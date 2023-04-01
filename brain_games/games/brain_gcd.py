import prompt
from brain_games.engine.engine_new import engine
from random import randint


def gcd_recursion(num1, num2):
    if num1 == 0:
        return num2
    return gcd_recursion(num2 % num1, num1)


def brain_gcd(welcome_message):
    # print(f'Find the greatest common divisor of given numbers.')
    counter = 1
    while counter <= 3:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        question = f'{num1} {num2}'
        correct_answer = str(gcd_recursion(num1, num2))
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        result = engine(welcome_message, correct_answer, answer, counter)
        if result == "Correct!":
            print(result)
            counter += 1
        else:
            return result
    print(engine(welcome_message, "", "", 3))
