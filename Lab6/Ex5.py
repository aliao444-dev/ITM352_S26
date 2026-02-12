# 1. Initialize Variables
age = 70
weekday = "Tuesday"
is_matinee = True

# 2. Determine applicable prices
# Start with the normal price
prices = [14]

# Senior discount
if age >= 65:
    prices.append(8)

# Tuesday discount
if weekday.lower() == "tuesday":
    prices.append(10)

# Matinee discount
if is_matinee:
    if age >= 65:
        prices.append(5)
    else:
        prices.append(8)

# 3. Find the lowest price
final_price = min(prices)

# 4. Print Results
print(f"--- Customer Ticket Info ---")
print(f"Age:      {age}")
print(f"Day:      {weekday}")
print(f"Matinee:  {is_matinee}")
print(f"-----------------------------")
print(f"Final Ticket Price: ${final_price}")