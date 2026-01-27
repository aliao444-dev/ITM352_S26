#This program demonstrates variable scope in Python
# Name: Anthony Liao
# Date: Jan 27, 2026

def calculate_discounted_price(price):
    #global discount
    discount = 0.9
    price = price * discount
    # price *= discount
    # the two lines above do the same thing
    print(f"Inside function, discounted price : {price:.2f}")
    return price

# the variable inside the function exists only within that function

discount = 0.6
price = 100
print(f"Original price before the function call : {price:.2f}")
discounted_price = calculate_discounted_price(price)

print(f"Original price after the function call : {price:.2f}")
print("Discount=", discount)

# This will cause an error because discount is not defined outside the function (5-12)
# Only after using 'global' keyword inside the function, it can be accessed outside
# It calls the global variable 'discount' instead of 0.6 because it's first and uses 'global'