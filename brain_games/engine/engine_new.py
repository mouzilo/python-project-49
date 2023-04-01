import prompt


def engine(welcome_message, question, correct_answer):
    counter = 0
    while counter < 3:
        print('Question:', question)
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. \n"
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {welcome_message}!")
            return

    print(f'Congratulations, {welcome_message}!')
