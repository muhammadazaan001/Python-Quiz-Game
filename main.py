name = input("Enter your name:")
questions ={"What is the capital of Pakistan?": "Islamabad",
            "How many continents are there on earth?": "8",
            "How many days are there in a week?": "7",
            "What is the name of the largest planet of the solar system?": "Jupitor"}

score = 0
for questions, correct_answers in questions.items():
    print(questions)
    user_answer = input("Enter Your Answer:")

    if user_answer.lower() == correct_answers.lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {correct_answers}.\n")

print(f"You got {score} out of 4 correct.")

with open("highscore.txt", "a") as file:
      file.write(f"{name} - {score} out of 4\n")
