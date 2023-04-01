from brain_games.games.brain_progression import brain_progression
from brain_games.scripts.brain_games import welcome_user


def progression():
    welcome_message = welcome_user()
    print('What number is missing in the progression?')
    brain_progression(welcome_message)


def main():
    progression()


if __name__ == '__main__':
    main()
