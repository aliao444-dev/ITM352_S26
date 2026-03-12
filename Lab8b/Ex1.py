# Initialize product data with numeric values for calculations
product = {
    "name": 'small gumball',
    "price": 0.34  # Converted from string '$0.34' to a float
}

# Define tax rate using standard snake_case naming
tax_rate = 0.045

# Calculate total price by adding the base price and the tax amount
total = product["price"] + (product["price"] * tax_rate)

# Output the result using dictionary keys and currency formatting
print(f"A {product['name']} costs ${total:.2f}")