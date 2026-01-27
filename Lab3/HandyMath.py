# Handy library of mathematical functions
# Name: Anthony Liao
# Date: Jan 27, 2026

def midpoint(num1, num2):
    """Calculate the midpoint between two numbers."""
    mid = (num1 + num2) / 2
    return mid

def sqrt(number):
    """Calculate the square root of a number."""
    if number < 0:
        return None  # Square root of negative number is not defined here
    return number ** 0.5

def exponent(base, exp):
    """Calculate the exponentiation of base raised to exp."""
    return base ** exp

