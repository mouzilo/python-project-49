#!/usr/bin/env python3


def brain_even():
    question = randint(1, 10)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return question, correct_answer


if __name__ == '__main__':
    brain_even()