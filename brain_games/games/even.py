from random import randint

RULES = 'Answer "yes" if number even, otherwise answer "no".'
MIN_NUM = 1
MAX_NUM = 999


def make_question_and_correct_answer():
    number = randint(MIN_NUM, MAX_NUM)
    question = str(number)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
