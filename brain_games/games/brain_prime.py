#!/usr/bin/env python3


from random import randint, choice


def brain_prime():
	# print(f'Answer "yes" if given number is prime. Otherwise answer "no".')
	counter = 0
	num = randint(1, 100)
	for i in range(2, num // 2+1):
		if (num % i == 0):
			counter += 1
	correct_answer = 'yes' if counter <= 0 else 'no'
	return num, correct_answer
