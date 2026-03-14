import os

# Dynamically construct the path to names.txt
file_path = os.path.join(os.path.dirname(__file__), "names.txt")

with open(file_path, "r") as f:
    # .read() grabs the entire file content as one large string
    content = f.read()

    # .splitlines() creates a list by breaking the string at each new line
    names_list = content.splitlines()

    print("Names list using .read():")
    print(content)
    print(f"Total number of names: {len(names_list)}")