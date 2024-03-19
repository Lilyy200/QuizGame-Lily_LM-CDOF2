import time



def get_questions():
    # Categorized questions by difficulty levels
    return {
        "Easy": [
        {"question": "What is 2 + 2?", "answer": "4"},
        {"question": "How many continents are there?", "answer": "7"},
        {"question": "What is the square root of 64?", "answer": "8"},
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is the color of the sky on a clear day?", "answer": "Blue"},
        {"question": "What is the first letter of the English alphabet?", "answer": "A"},
        {"question": "What shape is a stop sign?", "answer": "Octagon"},
    ],
    "Medium": [
        {"question": "What is the boiling point of water?", "answer": "100°C"},
        {"question": "What is the chemical symbol for water?", "answer": "H2O"},
        {"question": "What is the tallest mountain in the world?", "answer": "Mount Everest"},
        {"question": "What gas do plants absorb from the atmosphere for photosynthesis?", "answer": "Carbon dioxide"},
        {"question": "In which organ of the human body would you find the hippocampus?", "answer": "Brain"},
    ],
    "Hard": [
        {"question": "Who was the first person to walk on the Moon?", "answer": "Neil Armstrong"},
        {"question": "What is the largest ocean on Earth?", "answer": "Pacific Ocean"},
        {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
        {"question": "Who wrote 'Romeo and Juliet'?", "answer": "William Shakespeare"},
        {"question": "What is the currency of the United States?", "answer": "Dollar"},
        {"question": "What is the name of the longest river in South America?", "answer": "Amazon River"},
        {"question": "In physics, what is the term for the speed at which an object is moving at a specific moment?", "answer": "Instantaneous velocity"},
    ],
    }

def ask_questions(questions, level, time_limit):
    score = 0
    for q in questions[level]:
        print(f"Time remaining: {time_limit} seconds")
        user_answer = input(q["question"] + " ")
        
        start_time = time.time()
        
        while time.time() - start_time < time_limit:
            # Check if the answer is provided within the time limit
            if user_answer.strip():
                break
        
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
    time_limit_per_question = 15  # Set the time limit for each question (in seconds)

    for level in levels:
        print(f"Starting {level} level...")
        score = ask_questions(all_questions, level, time_limit_per_question)
        total_score += score
        print(f"Your score for {level} level is {score}")

    # Final score and message
    print(f"Final Score: {total_score}")

if __name__ == "__main__":
    main()
