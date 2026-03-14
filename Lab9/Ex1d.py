import os

# Dynamically construct the path to names.txt
file_path = os.path.join(os.path.dirname(__file__), "names.txt")

with open(file_path, "r") as f:
    count = 0
    # .readline() reads exactly one line at a time
    line = f.readline()

    print("Names list using .readline():")
    while line:
        # .strip() removes the invisible newline character (\n)
        print(line.strip())
        count += 1
        # Move to the next line
        line = f.readline()

    print(f"Total number of names: {count}")
