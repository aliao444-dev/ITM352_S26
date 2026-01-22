# Ask the user to enter a teperature in fahrenheit
# Convert the temperature to celsius using the formula: °C = (°F – 32) × (5/9)).
# Name: Anthony Liao
# Date: Jan 22, 2026

fahrenheit_input = input("Please enter a temperature in Fahrenheit: ")
fahrenheit_value = float(fahrenheit_input)
celsius_value = (fahrenheit_value - 32) * 5 / 9
celsius_value_rounded = round(celsius_value, 1)

print("You entered:", fahrenheit_value)
print(f"The temperature in Celsius is:, {celsius_value_rounded}")