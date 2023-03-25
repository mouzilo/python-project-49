#!/usr/bin/env python3


import prompt
from random import randint, choice
from ..welcome.cli import welcome_user


def main():
    welcome_message = welcome_user()
    counter = 0
    while counter < 3:
        print('What is the result of the expression?')
        rand_int1 = randint(1, 10)
        rand_int2 = randint(1, 10)
        operator = choice(["+", "-", "*"])

        print(f'Question: {rand_int1} {operator} {rand_int2}')
        answer = input('Answer: ')

        if str(eval(f'{rand_int1} {operator} {rand_int2}')) == answer:
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{eval(str(rand_int1) + operator + str(rand_int2))}'.\nLet's try again, {welcome_message}!")
            return
    print(f'Congratulations, {welcome_message}!')


if __name__ == '__main__':
    main()