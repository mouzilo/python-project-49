#!/usr/bin/env python3


import prompt
from random import randint, choice
from brain_games.welcome.cli import welcome_user
from brain_games.games.brain_even import even
from brain_games.games.brain_calc import calc


def calc_s():
	calc()


def even_s():
	even()