# Write Python code that uses the input built-in function to ask the user to enter the year they were born
# as a four-digit number. The input function always returns a string value,
# so use the int built-in function to convert the year value entered to an integer data type
# and subtract the year entered from the current year (e.g., 2019).
# Print a message to the user stating the value that they entered and their calculated age. 


birth_year = input("Please enter your birth year: ")
birth_year_int = int(birth_year)
current_year = 2026
age = current_year - birth_year_int
print("You entered:", birth_year)
print(f"You are {age} years old,")