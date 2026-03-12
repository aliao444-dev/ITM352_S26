import json  # Corrected import

QUESTION = {
    "What is the airspeed of an unladen swallow in miles/hr?": {"12", "10", "15", 8},
    "What is the capital of Texas?": {"Austin", "Houston", "Dallas"},
    "The Last Supper was painted by which artist?": {"Leonardo da Vinci", "Michelangelo", "Raphael"}
}

filename = "quiz_data.json"

with open(filename, "r") as file:
    data = json.load(file)

for question in data["questions"]:
    print(f"Question: {question['question']}")
    print("Answers:")
    for answer in question['answers']:
        print(f"- {answer}")
    print()