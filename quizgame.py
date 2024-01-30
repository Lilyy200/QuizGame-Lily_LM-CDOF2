def get_questions():
    # Categorized questions by difficulty levels
    return {
        "Easy": [
            {"question": "What is 2 + 2?", "answer": "4"},
            {"question": "How many continents are there?", "answer": "7"},
            {"question": "What is the square root of 64?", "answer": "8"},
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "What is the color of the sky on a clear day?", "answer": "Blue"},
        ],
        "Medium": [
            {"question": "What is the boiling point of water?", "answer": "100°C"},
            {"question": "What is the chemical symbol for water?", "answer": "H2O"},
            {"question": "What is the tallest mountain in the world?", "answer": "Mount Everest"},
        ],
        "Hard": [
            {"question": "Who was the first person to walk on the Moon?", "answer": "Neil Armstrong"},
            {"question": "What is the largest ocean on Earth?", "answer": "Pacific Ocean"},
            {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
            {"question": "Who wrote 'Romeo and Juliet'?", "answer": "William Shakespeare"},
            {"question": "What is the currency of the United States?", "answer": "Dollar"},
        ]
    }

def ask_questions(questions, level):
    score = 0
    for q in questions[level]:
        user_answer = input(q["question"] + " ")
        if user_answer.lower() == q["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The answer was {q['answer']}")
    return score

def main():
    all_questions = get_questions()
    levels = ["Easy", "Medium", "Hard"]
    total_score = 0

    for level in levels:
        print(f"Starting {level} level...")
        score = ask_questions(all_questions, level)
        total_score += score
        print(f"Your score for {level} level is {score}")

    # Final score and message
    print(f"Final Score: {total_score}")

if __name__ == "__main__":
    main()