
def get_questions():
    # Returns a list of questions and answers
    return [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is 2 + 2?", "answer": "4"},
        {"question": "What is the color of the sky on a clear day?", "answer": "Blue"}
    ]

def ask_questions(questions):
    score = 0
    for q in questions:
        user_answer = input(q["question"] + " ")
        if user_answer.lower() == q["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The answer was {q['answer']}")
    return score

def main():
    questions = get_questions()
    score = ask_questions(questions)
    if score == 3:
        print(f"Congratulations! You've won the game with a perfect score of {score}/3!")
    else:
        print(f"Game Over. You lost. Your score was {score}/3")

if __name__ == "__main__":
    main()


