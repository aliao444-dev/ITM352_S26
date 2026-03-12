# Opening the file in read mode ('r')
f = open("names.txt", "r")

# Displaying the type of the object returned by open()
print(f"Data type of open(): {type(f)}")

# Manual close is required when not using a context manager
f.close()

# WHY THIS IS USEFUL:
# The open() function returns a file object (a stream) rather than the raw data. 
# This is useful because it allows Python to handle large files efficiently by 
# buffering data, meaning it doesn't have to load a 10GB file into your RAM 
# all at once just to read the first line.