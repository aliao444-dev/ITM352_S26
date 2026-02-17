def is_leap_year(year):
    # (Condition A AND Condition B) OR Condition C
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Get input from the user
user_input = input("Enter your birth year: ")

# Convert the string input to an integer
birth_year = int(user_input)

# Check and print the result
if is_leap_year(birth_year):
    print(f"{birth_year} is a leap year! Nice.")
else:
    print(f"{birth_year} is not a leap year.")