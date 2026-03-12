with open("names.txt") as file_object:
    contents_list = file_object.readlines()
    print(contents_list)
    print(f"Number of names: {len(contents_list)}")

with open("names.txt", "a") as file_object:
    print("Appending new name to the file...")
    file_object.write("Adams, Amy\n")
    contents_list.append("Adams, Amy")
    # By doing both the append and the write, we ensure that our in-memory list and the file are both updated.
    print(f"Number of names after appending: {len(contents_list)}")