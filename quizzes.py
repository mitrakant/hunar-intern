
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. Ernest Hemingway", "D. F. Scott Fitzgerald"],
        "answer": "A"
    }
]


def ask_questions(questions):
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {q['answer']}.")
        print()
    return score


def display_score(score, total):
    print(f"Your final score is {score}/{total}.")
    print(f"Your percentage is {score / total * 100:.2f}%")


def main():
    print("Welcome to the Quiz!")
    print("Please answer the following questions:")
    print()
    
    score = ask_questions(questions)
    display_score(score, len(questions))

if __name__ == "__main__":
    main()
