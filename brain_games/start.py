#!/usr/bin/env python3

from brain_games.engine import engine
from brain_games.games.brain_games import brain_games


def welcome():
    brain_games()


def calc():
    engine(game='brain_calc')


def even():
    engine(game='brain_even')


def gcd():
    engine(game='brain_gcd')


def progression():
    engine(game='brain_progression')


def prime():
    engine(game='brain_prime')
