#!/usr/bin/env python3


from random import randint, choice


def brain_even():
    question = randint(1, 10)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return question, correct_answer