# Define a list of item prices
prices = [5.95, 3.00, 12.50]
total_price = 0

# Set the tax multiplier (1.00 + 0.08 tax rate)
tax_rate = 1.08

# Iterate through each price, applying tax and accumulating the sum
for price in prices:
    total_price += price * tax_rate

# Display the final formatted total
print(f"Total price (with tax): ${total_price:.2f}")