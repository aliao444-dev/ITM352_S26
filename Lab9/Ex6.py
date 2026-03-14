import json
import os

# Dynamically construct the path to quiz_questions.json
file_path = os.path.join(os.path.dirname(__file__), "quiz_questions.json")

# Read and print the JSON file
with open(file_path, "r") as infile:
    quiz_questions = json.load(infile)
    print(json.dumps(quiz_questions, indent=4))

# Advantages of JSON:
# - Human-readable and easy to understand.
# - Lightweight and widely used for data exchange.
# - Supported by most programming languages.
# - Can represent complex data structures (e.g., nested objects).

# Disadvantages of JSON:
# - No support for comments, which can make documentation harder.
# - Limited data types (e.g., no support for dates or custom objects).
# - Can be less efficient than binary formats for large datasets.