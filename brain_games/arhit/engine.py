import prompt


MAX_SCORE = 3


def run_game(game_name):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!")
    print(game_name.RULES)
    round_number = 1

    while round_number <= MAX_SCORE:
        question, correct_answer = game_name.make_question_and_correct_answer()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')

        if not (correct_answer == user_answer):
            print(f"'{user_answer}' is wrong answer ;(.")
            print(f"Correct answer was '{correct_answer}'.")
            print(f"let's try again, {user_name}!")
            break

        print('Correct!')
        round_number += 1
    else:
        print(f"Congratulations, {user_name}!")
