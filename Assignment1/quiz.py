"""
quiz.py - Interactive Multiple-Choice Quiz Application
Author: Anthony
Description: Loads questions from a JSON file and runs an interactive quiz,
             validating user input and reporting a final score.
"""

import json
import os


def load_questions(filename):
    """
    Load quiz questions from a JSON file.

    Each question in the file should have:
      - "question": the question text
      - "options": a dict mapping letters (a-d) to answer text
      - "answer": the correct letter (e.g. "c")

    Returns a list of question dictionaries, or an empty list if the file
    cannot be read.
    """
    try:
        with open(filename, "r") as f:
            questions = json.load(f)
        return questions
    except FileNotFoundError:
        print(f"Error: Question file '{filename}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: '{filename}' is not valid JSON.")
        return []


def ask_question(number, question_data):
    """
    Display a single question and collect a valid answer from the user.

    Keeps re-prompting until the user enters one of the valid option letters.
    Returns True if the user's answer is correct, False otherwise.

    Parameters:
        number       (int)  : Question number to display (1-based)
        question_data (dict): A single question dictionary from the loaded file
    """
    valid_choices = list(question_data["options"].keys())

    # Display the question and all answer options
    print(f"\nQuestion {number}: {question_data['question']}")
    for letter, text in question_data["options"].items():
        print(f"  {letter}) {text}")

    # Keep prompting until a valid option is entered
    while True:
        user_answer = input("Your answer: ").strip().lower()
        if user_answer in valid_choices:
            break
        print(f"Invalid choice. Please enter one of: {', '.join(valid_choices)}")

    # Check and report correctness
    correct = question_data["answer"]
    if user_answer == correct:
        print("Correct!")
        return True
    else:
        print(f"Wrong. The correct answer was: {correct}) {question_data['options'][correct]}")
        return False


def run_quiz(questions):
    """
    Run through all questions and track the user's score.

    Parameters:
        questions (list): List of question dictionaries loaded from file

    Returns:
        score (int): Number of correct answers
    """
    score = 0
    for i, question_data in enumerate(questions, start=1):
        if ask_question(i, question_data):
            score += 1
    return score


# ── Main program ──────────────────────────────────────────────────────────────

QUESTIONS_FILE = os.path.join(os.path.dirname(__file__), "questions.json")

print("=" * 40)
print("      Welcome to the Python Quiz!")
print("=" * 40)

# Load questions from file
questions = load_questions(QUESTIONS_FILE)

if not questions:
    print("No questions available. Please check the questions file.")
else:
    total = len(questions)
    print(f"\nThis quiz has {total} questions. Good luck!\n")

    # Run the quiz and collect the final score
    final_score = run_quiz(questions)

    # Display the final results
    print("\n" + "=" * 40)
    print(f"Quiz complete! You scored {final_score} out of {total}.")
    percentage = (final_score / total) * 100
    print(f"That's {percentage:.1f}%.")

    # Give a simple performance message
    if percentage == 100:
        print("Perfect score - excellent work!")
    elif percentage >= 70:
        print("Good job!")
    else:
        print("Keep studying - you'll get there!")

    print("=" * 40)
