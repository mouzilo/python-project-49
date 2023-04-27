from random import randint

START_GEN = 1
LENGTH = 10
STEP = 2
DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(start=START_GEN, length=LENGTH, step=STEP):
    progression = []
    for i in range(length):
        progression.append(start + i * step)
    return progression


def generate_question():
    progression = generate_progression()
    hidden_index = randint(0, len(progression) - 1)
    correct_answer = str(progression[hidden_index])
    progression_with_hidden = list(map(str, progression))
    progression_with_hidden[hidden_index] = '..'
    question = str(' '.join(progression_with_hidden))
    return question, correct_answer
