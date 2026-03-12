# STEP 1: Use 'a' (append) mode to add to the end without deleting existing data
with open("names.txt", "a") as f:
    f.write("\nAnthony Liao")

# STEP 2: Re-open in 'r' mode to see the updated contents
with open("names.txt", "r") as f:
    print("Updated file contents:")
    print(f.read())

# PROS OF APPENDING: Safe; preserves existing data. Good for logs.
# CONS OF APPENDING: You can't edit existing lines; you can only add to the bottom.

# PROS OF OVERWRITING ('w'): Good for refreshing a data file completely.
# CONS OF OVERWRITING: Destructive; if you make a mistake, the old data is gone forever.