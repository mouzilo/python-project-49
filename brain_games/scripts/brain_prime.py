from brain_games.games.brain_prime import brain_prime
from brain_games.engine.engine_new import engine
from brain_games.games.brain_games import welcome_user


def prime():
    welcome_message = welcome_user()
    print(f'Answer "yes" if given number is prime. '
          f'Otherwise answer "no".')
    question, correct_answer = brain_prime()
    engine(welcome_message, question, correct_answer)


def main():
    prime()


if __name__ == '__main__':
    main()