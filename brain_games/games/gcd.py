from math import gcd
from random import randint

RULES = 'Find the greatest common divisor of given numbers'


def make_question_and_correct_answer():
    min_num = 1
    max_num = 99
    number_first = randint(min_num, max_num)
    number_second = randint(min_num, max_num)
    question = f"{number_first} {number_second}"
    correct_answer = gcd(number_first, number_second)
    return question, str(correct_answer)
