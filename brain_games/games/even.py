from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question_and_correct_answer():
    number = randint(1, 100)
    question = str(number)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
