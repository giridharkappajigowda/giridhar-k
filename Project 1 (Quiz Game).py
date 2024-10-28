fquiz_questions = {
    "What is the process of finding errors in software code?": {
        "A": "Hacking",
        "B": "Compiling",
        "C": "Testing",
        "D": "Debugging",
        "Correct": "D"
    },
    "What shares hardware,software,and data among authorized users?": {
        "A": "Protocol",
        "B": "Network",
        "C": "Hyperlink",
        "D": "Transmitter",
        "Correct": "B"
    },
    "What is the process of carrying out the command'?": {
        "A": "Executing",
        "B": "Fetching",
        "C": "Storing",
        "D": "Decoding",
        "Correct": "A"
    }
}

def quiz_game():
    score = 0
    for question, options in quiz_questions.items():
        print(question)
        for option, value in options.items():
            if option != "Correct":
                print(f"{option}: {value}")
        answer = input("Enter your answer (A, B, C, D): ")
        if answer.upper() == options["Correct"]:
            print("Correct answer!")
            score += 1
        else:
            print(f"Incorrect answer. The correct answer is {options['Correct']}.")
    print(f"\nYour final score is {score} out of {len(quiz_questions)}.")

def main():
    print("Welcome to the Quiz Game!")
    quiz_game()

if __name__ == "__main__":
    main()