import prompt


MAX_ROUNDS = 3


def run(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!")
    print(game.RULES)

    for _ in range(MAX_ROUNDS):
        question, correct_answer = game.make_question_and_correct_answer()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')

        if not (correct_answer == user_answer):
            print(f"'{user_answer}' is wrong answer ;(.")
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            break

        print('Correct!')
    else:
        print(f"Congratulations, {user_name}!")
