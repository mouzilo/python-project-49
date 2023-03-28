#!/usr/bin/env python3


import prompt
from random import randint, choice
from brain_games.engine import engine
from brain_games.games.brain_games import welcome_user, brain_games


def welcome():
	brain_games()


def calc():
	engine(game = 'brain_calc')


def even():
	engine(game = 'brain_even')


def gcd():
	engine(game = 'brain_gcd')