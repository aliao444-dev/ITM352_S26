# Parse through the portions of an email address
# Name: Anthony Liao
# Date: Feb 3, 2026

email = input("Enter your email address: ")

parts = email.split("@")
username = parts[0]
domain_ = parts[1]

print("Username:", username)
print("Domain:", domain_)

# Method 2: Using index and slicing

at_symbol_index = email.index("@")
username2 = email[:at_symbol_index]
domain2 = email[at_symbol_index + 1 :]

# index() method finds the first occurrence of the specified value

print("Username (method 2):", username2)
print("Domain (method 2):", domain2)

