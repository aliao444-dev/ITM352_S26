# Multiply two numbers by adding the first number to itself 'y' times
def multiply(x, y):
    product = 0
    for _ in range(y):
        product += x
    return product

# Convert user input to integers for calculation
try:
    first = int(input("Enter the first number: "))
    second = int(input("Enter the second number: "))
    
    prod = multiply(first, second)
    print(f"The product of {first} and {second} is {prod}")
except ValueError:
    print("Please enter valid integers.")