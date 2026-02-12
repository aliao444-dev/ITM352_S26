def is_leap_year(year):
    # (Condition A AND Condition B) OR Condition C
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)