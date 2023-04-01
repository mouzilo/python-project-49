from brain_games.games.brain_calc import brain_calc
from brain_games.engine.engine_new import engine
from brain_games.games.brain_games import welcome_user


def calc():
    welcome_message = welcome_user()
    print('What is the result of the expression?')
    question, correct_answer = brain_calc()
    engine(welcome_message, question, correct_answer)


def main():
    calc()


if __name__ == '__main__':
    main()