def isLeapYear(year):
    # Rule 1: Most specific exception first
    if year % 400 == 0:
        return "Leap year"
    
    # Rule 2: The century exception
    if year % 100 == 0:
        return "Not a leap year"
    
    # Rule 3: The general rule
    if year % 4 == 0:
        return "Leap year"
    
    # Rule 4: Everything else
    return "Not a leap year"