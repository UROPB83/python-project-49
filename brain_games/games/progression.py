from random import randint

RULES = 'What numb is miss in the progression?'


def generate_progression():
    step = randint(1, 5)
    start = randint(1, 100)
    stop = start + (step * 10)

    progression = [str(x) for x in range(start, stop, step)]

    return progression


def make_question_and_correct_answer():
    progression = generate_progression()
    skip = randint(0, 9)
    correct = progression[skip]
    progression[skip] = ".."
    question = " ".join(progression)
    return (question, correct)
