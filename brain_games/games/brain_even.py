from random import randint


def brain_even():
    # print(f'Answer "yes" if the number is even, otherwise answer "no".')
    question = randint(1, 10)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return question, correct_answer
