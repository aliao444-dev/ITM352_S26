data = ("hello", 10, "goodbye", 3, "welcome", 5, 6, 7, True)

string_count = 0

for item in data:
    if type(item) == str:
        string_count += 1


# data is a tuple, it's iterable, so we can use a for loop to go through each item in the tuple and check if it's a string using isinstance() function. If it is a string, we increment the string_count variable by 1. Finally, we print the total count of strings in the tuple.
# type returns the variable's type, and we can compare it to the str type to check if it's a string. We could also use isinstance(item, str) which is a more flexible way to check for string types, as it would also return True for subclasses of str.

print(f"There are {string_count} strings in the data tuple.")