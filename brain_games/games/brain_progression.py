from random import randint

START_GEN = 1
END_GEN = 10


def generate_question():
    a = randint(START_GEN, END_GEN)
    d = randint(START_GEN, END_GEN)
    progression = []
    for i in range(10):
        progression.append(a + i * d)
    hidden_index = randint(0, len(progression) - 1)
    correct_answer = str(progression[hidden_index])
    progression_with_hidden = list(map(str, progression))
    progression_with_hidden[hidden_index] = '..'
    question = str(' '.join(progression_with_hidden))
    return question, correct_answer
