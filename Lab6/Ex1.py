# Initialize a tuple of emotions
emotions = ("happy", "sad", "fear", "surprise")


# Use conditional expression to check if last element is "happy" and len > 3
# Using and/or logic without if-statement or ternary operator
result = (emotions[-1] == "happy" and len(emotions) > 3 and "true") or "false"
print(result)


