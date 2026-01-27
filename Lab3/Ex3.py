def sqrt(number):
    "Calculate the square root of a numberbr"
    if number < 0:
        return None
    return number ** 0.5


#number = float(input("Enter a number: "))
#result = sqrt(number)
#if result is None:
    print("Error: Cannot compute the square root of a negative number.")
#else:
    print(f"The square root of {number} is {result}")

    number_in = float(input("Enter a positive number to find its square root: "))

number_a = float(input("Enter a positive number to find its square root: "))
result = sqrt(number_a)
if result is None:
    print("Error: Cannot compute the square root of a negative number.")
else:
    print(f"The square root of {number_a5} is {result}")