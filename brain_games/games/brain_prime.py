from random import randint


def brain_prime():

    counter = 0
    num = randint(1, 100)
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            counter += 1
    correct_answer = 'yes' if counter <= 0 else 'no'
    return num, correct_answer
