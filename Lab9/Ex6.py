import json
import os

# Dynamically construct the path to quiz_questions.json
file_path = os.path.join(os.path.dirname(__file__), "quiz_questions.json")

# Read and print the JSON file
with open(file_path, "r") as infile:
    quiz_questions = json.load(infile)
    print(json.dumps(quiz_questions, indent=4))
