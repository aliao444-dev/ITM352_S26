with open("names.txt", "r") as f:
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

# WHEN TO USE: Use .readline() for massive files where you only need to 
# process one line at a time to save memory, or if you only need the first 
# few lines (like a header). 
# DON'T USE: If you need to sort the data or access it randomly (e.g., jumping 
# from the bottom to the top), as this method only moves forward.