def engine(message, generate_question_func):

    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print(message)

    correct_answers_count = 0
    for question_num in range(1, 4):
        question, correct_answer = generate_question_func()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. \n"
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return False
    print(f'Congratulations, {name}!')
    return True
