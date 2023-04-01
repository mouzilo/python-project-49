from random import randint


def brain_progression():

    a = randint(1, 10)
    d = randint(1, 10)
    progression = []
    for i in range(10):
        progression.append(a + i * d)

    hidden_index = randint(0, len(progression) - 1)
    hidden_number = str(progression[hidden_index])
    progression_with_hidden = list(map(str, progression))
    progression_with_hidden[hidden_index] = '..'

    return ' '.join(progression_with_hidden), hidden_number
