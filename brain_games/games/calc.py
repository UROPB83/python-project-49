from random import choice, randint
from operator import sub, add, mul

RULES = 'What is the result of the expression?'
OPERATIONS = [("+", add), ("-", sub), ("*", mul)]


def make_question_and_correct_answer():
    a = randint(1, 20)
    b = randint(1, 20)

    operator, func = choice(OPERATIONS)

    correct_answer = func(a, b)
    question = f"{a} {operator} {b}"
    return question, str(correct_answer)
