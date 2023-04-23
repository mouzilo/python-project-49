ROUND_START = 1
ROUND_END = 4


def engine(game_module):

    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    game_module.print_description()

    correct_answers_count = 0
    for question_num in range(ROUND_START, ROUND_END):
        question, correct_answer = game_module.generate_question()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. \n"
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
    return True
