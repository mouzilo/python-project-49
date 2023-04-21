import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def engine(welcome_message, generate_question_func):
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
                  f"Let's try again, {welcome_message}!")
            return False
    print(f'Congratulations, {welcome_message}!')
    return True
