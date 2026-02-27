# Quiz game. Fourth version.
# Name: Anthony Liao
# Date: Feb 24, 2026
# Make a list with the questions and correct answers.
# Make QUESTIONS a dictionary, to include answer options and the correct choice.
# Allow the user to select the correct answer by a label


QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr?": ["12", "10", "15", "8"],
    "What is the capital of Texas?": ["Austin", "Houston", "Dallas", "San Antonio"],
    "The last supper was painted by which artist?": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Donatello"],
    }

for question, options in QUESTIONS.items():
    correct_answer = options [0]  # Assuming the first option is the correct answer
    for label, alternative in enumerate(sorted(options), start=1):
        print(f"  {label}) {alternative}")

    try:
        answer_label = int(input(question + " "))
    except ValueError:
        print("Please enter a number.")
        continue
    answer = sorted(options)[answer_label - 1]  # Convert label to index
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is '{correct_answer}', not '{answer!r}'.")