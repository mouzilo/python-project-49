#!/usr/bin/env python3


import prompt
from random import randint
from ..welcome.cli import welcome_user


def even():
    welcome_message = welcome_user()
    counter = 0
    while counter < 3:
        print('Answer "yes" if the number is even, otherwise answer "no".')
        rand_int = randint(1, 10)
        print(f'Question: {rand_int}')
        answer = input('Answer: ')
        if (answer.casefold() == 'yes' and rand_int % 2 == 0) or \
                (answer.casefold() == 'no' and rand_int % 2 == 1):
            print('Correct!')
            counter += 1
        elif answer.casefold() == 'no' and rand_int % 2 == 0:
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'. \nLet's try again, {welcome_message}!")
            return
        elif answer.casefold() == 'yes' and rand_int % 2 == 1:
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'. \nLet's try again, {welcome_message}!")
            return
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'. \nLet's try again, {welcome_message}!")
            return
    print(f'Congratulations, {welcome_message}!')


def main():
    even()


if __name__ == '__main__':
    main()
