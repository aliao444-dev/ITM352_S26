import json
import os

# Dynamically construct the path to questions.json
input_file_path = os.path.join(os.path.dirname(__file__), "../Assignment1/questions.json")
output_file_path = os.path.join(os.path.dirname(__file__), "quiz_questions.json")

# Load the dictionary of quiz questions
with open(input_file_path, "r") as infile:
    quiz_questions = json.load(infile)

# Save the dictionary as a JSON file
with open(output_file_path, "w") as outfile:
    json.dump(quiz_questions, outfile, indent=4)

print(f"Quiz questions saved to {output_file_path}")