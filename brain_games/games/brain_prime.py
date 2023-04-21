from random import randint

START_GEN = 1
END_GEN = 10


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_question():
    question = randint(START_GEN, END_GEN)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer
