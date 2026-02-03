# String Methods Testing

# Test isnumeric()
print("=== isnumeric() ===")
test_str1 = "12345"
test_str2 = "123.45"
test_str3 = "abc"
test_str4 = "123abc"

print(f"'{test_str1}'.isnumeric(): {test_str1.isnumeric()}")  # True
print(f"'{test_str2}'.isnumeric(): {test_str2.isnumeric()}")  # False (contains dot)
print(f"'{test_str3}'.isnumeric(): {test_str3.isnumeric()}")  # False
print(f"'{test_str4}'.isnumeric(): {test_str4.isnumeric()}")  # False
print()

# Test upper()
print("=== upper() ===")
test_str5 = "hello world"
test_str6 = "PyThOn 123"
test_str7 = "ALREADY UPPERCASE"

print(f"'{test_str5}'.upper(): '{test_str5.upper()}'")
print(f"'{test_str6}'.upper(): '{test_str6.upper()}'")
print(f"'{test_str7}'.upper(): '{test_str7.upper()}'")
print()

# Test isalpha()
print("=== isalpha() ===")
test_str8 = "abcdef"
test_str9 = "abc123"
test_str10 = "hello world"
test_str11 = "OnlyLetters"

print(f"'{test_str8}'.isalpha(): {test_str8.isalpha()}")   # True
print(f"'{test_str9}'.isalpha(): {test_str9.isalpha()}")   # False
print(f"'{test_str10}'.isalpha(): {test_str10.isalpha()}")  # False (has space)
print(f"'{test_str11}'.isalpha(): {test_str11.isalpha()}")  # True