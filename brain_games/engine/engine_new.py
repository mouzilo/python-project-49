def engine(welcome_message, correct_answer, answer, counter):
    if counter == 1 or counter == 2:
        if answer == correct_answer:
            return 'Correct!'
        else:
            print(f"'{answer}' is wrong answer ;(. \n"
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {welcome_message}!")
            return
    else:
        if answer == correct_answer:
            print(f'Congratulations, {welcome_message}!')
        else:
            print(f"'{answer}' is wrong answer ;(. \n"
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {welcome_message}!")
            return
