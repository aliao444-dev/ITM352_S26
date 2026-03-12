# REWRITE USING 'WITH':
with open("names.txt", "r") as f:
    data = f.read()
    print("File opened and read successfully.")

# WHY CLOSE A FILE: It is good practice to close files to free up system 
# resources (memory/file handles). If a file is left open, other programs 
# might be blocked from using it, and data might not be saved correctly.

# BENEFITS OF 'WITH': The 'with' statement is a context manager that 
# automatically closes the file for you as soon as the code block ends, 
# even if your program crashes or hits an error inside the block.