from brain_games.games.brain_even import brain_even
from brain_games.scripts.brain_games import welcome_user


def even():
    welcome_message = welcome_user()
    print('Answer "yes" if the number is even, '
          'otherwise answer "no".')
    brain_even(welcome_message)


def main():
    even()


if __name__ == '__main__':
    main()
