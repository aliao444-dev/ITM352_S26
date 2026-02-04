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
# index() method finds the first occurrence of the specified value


at_symbol_index = email.index("@")
username_manual = email[:at_symbol_index]
domain_manual = email[at_symbol_index + 1 :]


print("Username (method 2):", username_manual)
print("Domain (method 2):", domain_manual)