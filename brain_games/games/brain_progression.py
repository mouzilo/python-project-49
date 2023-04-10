from brain_games.engine.engine import engine
from random import randint


def brain_progression(welcome_message):
    print('What number is missing in the progression?')
    start_gen = 1
    end_gen = 10

    def generate_question():
        a = randint(start_gen, end_gen)
        d = randint(start_gen, end_gen)
        progression = []
        for i in range(10):
            progression.append(a + i * d)
        hidden_index = randint(0, len(progression) - 1)
        correct_answer = str(progression[hidden_index])
        progression_with_hidden = list(map(str, progression))
        progression_with_hidden[hidden_index] = '..'
        question = str(' '.join(progression_with_hidden))
        return question, correct_answer

    engine(welcome_message, generate_question)
