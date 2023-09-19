from math import gcd
from random import randint

RULES = 'Find the greatest common divisor of given numbers.'


def make_question_and_correct_answer():
    number_first = randint(1, 99)
    number_second = randint(1, 99)
    question = f"{number_first} {number_second}"
    correct_answer = gcd(number_first, number_second)
    return question, str(correct_answer)
