#!/usr/bin/env python3


import prompt

#функция для всех прочих игр
def welcome_user():
    name = prompt.string('May I have your name? ')
    return name
    
#функция для игры brain-games
def brain_games():
    name = prompt.string('May I have your name? ')
    print (f'Hello, {name}!')


def main():
    name = prompt.string('May I have your name? ')
    return (f'Hello, {name}!')


if __name__ == '__main__':
    main()