import prompt

ROUND_COUNT = 3


def engine(game_module):

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_module.DESCRIPTION)

    for question_num in range(ROUND_COUNT):
        question, correct_answer = game_module.generate_question()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. \n"
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
    return
