from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return False
    for i in range(2, (number // 2 + 1)):
        if number % i == 0:
            return False
    return True


def make_question_and_correct_answer():
    number = randint(1, 100)
    question = str(number)

    if is_prime(number):
        correct_answer = 'yes'

    else:
        correct_answer = 'no'

    return str(question), str(correct_answer)
