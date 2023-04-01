import prompt
from brain_games.engine.engine_new import engine
from random import randint


def brain_progression(welcome_message):
    counter = 1
    while counter <= 3:
        a = randint(1, 10)
        d = randint(1, 10)
        progression = []
        for i in range(10):
            progression.append(a + i * d)
        hidden_index = randint(0, len(progression) - 1)
        correct_answer = str(progression[hidden_index])
        progression_with_hidden = list(map(str, progression))
        progression_with_hidden[hidden_index] = '..'
        question = str(' '.join(progression_with_hidden))
        print(question)
        answer = prompt.string('Your answer: ')
        result = engine(welcome_message, correct_answer, answer, counter)
        if result == "Correct!":
            print(result)
            counter += 1
        else:
            return result
    print(engine(welcome_message, "", "", 3))
