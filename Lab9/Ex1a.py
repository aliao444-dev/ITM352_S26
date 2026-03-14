import os

# Dynamically construct the path to names.txt
file_path = os.path.join(os.path.dirname(__file__), "names.txt")

# Opening the file in read mode ('r')
f = open(file_path, "r")

# Displaying the type of the object returned by open()
print(f"Data type of open(): {type(f)}")

# Manual close is required when not using a context manager
f.close()

