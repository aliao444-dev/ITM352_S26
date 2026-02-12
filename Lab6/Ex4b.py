def isLeapYear(year):
    # Rule 1: Most specific exception first (centuries divisible by 400)
    if year % 400 == 0:
        return "Leap year"
    
    # Rule 2: Other centuries are NOT leap years
    if year % 100 == 0:
        return "Not a leap year"
    
    # Rule 3: General rule (divisible by 4)
    if year % 4 == 0:
        return "Leap year"
    
    # Rule 4: Everything else
    return "Not a leap year"

# Testing with input
user_input = input("Enter your birth year: ")
birth_year = int(user_input)
print(f"Result: {isLeapYear(birth_year)}")