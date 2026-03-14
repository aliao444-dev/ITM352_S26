import os

# Dynamically construct the path to names.txt
file_path = os.path.join(os.path.dirname(__file__), "names.txt")

# REWRITE USING 'WITH':
with open(file_path, "r") as f:
    data = f.read()
    print("File opened and read successfully.")

