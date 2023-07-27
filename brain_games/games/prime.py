from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return "no"
    for i in range(2, (number // 2 + 1)):
        if number % i == 0:
            return "no"
    return "yes"


def make_question_and_correct_answer():
    min_num = 1
    max_num = 21
    number = randint(min_num, max_num)
    question = str(number)
    return question, is_prime(number)
