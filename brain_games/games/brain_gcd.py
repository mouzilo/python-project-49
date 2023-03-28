#!/usr/bin/env python3


from random import randint, choice


def gcd_recursion(num1, num2):
    if num1 == 0:
        return num2
    return gcd_recursion(num2 % num1, num1)


def brain_gcd():
    # print(f'Find the greatest common divisor of given numbers.')
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = f'{num1} {num2}'
    correct_answer = str(gcd_recursion(num1, num2))
    return question, correct_answer