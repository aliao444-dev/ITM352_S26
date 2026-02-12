# Test cases: [list, expected_condition]
test_cases = [
    # Condition 1: fewer than 5 elements
    ([], "fewer than 5"),                                # 0 elements - boundary
    ([1], "fewer than 5"),                              # 1 element
    ([1, 2, 3], "fewer than 5"),                        # 3 elements
    (["a", "b", "c", "d"], "fewer than 5"),             # 4 elements - boundary
    
    # Condition 2: between 5 and 10 elements (inclusive)
    ([1, 2, 3, 4, 5], "between 5 and 10"),              # 5 elements - lower boundary
    ([1, 2, 3, 4, 5, 6, 7], "between 5 and 10"),        # 7 elements
    (list(range(10)), "between 5 and 10"),              # 10 elements - upper boundary
    
    # Condition 3: more than 10 elements
    (list(range(11)), "more than 10"),                  # 11 elements - boundary
    (list(range(15)), "more than 10"),                  # 15 elements
    (list(range(100)), "more than 10"),                 # 100 elements
]

# Test each case and verify results
print("=" * 60)
print("TESTING CONDITIONS ON LISTS OF DIFFERENT LENGTHS")
print("=" * 60)

for my_list, expected in test_cases:
    print(f"\nTest case: {len(my_list)} elements")
    print(f"Expected: {expected}")
    print(f"List: {my_list if len(my_list) <= 10 else f'{my_list[:5]}... (truncated)'}")
    
    # Apply the conditional logic
    if len(my_list) < 5:
        result = "fewer than 5"
        print("Result: This list has fewer than 5 elements.")
    elif 5 <= len(my_list) <= 10:
        result = "between 5 and 10"
        print("Result: This list has between 5 and 10 elements (inclusive).")
    else:
        result = "more than 10"
        print("Result: This list has more than 10 elements.")
    
    # Verify the result matches expected
    if result == expected:
        print("PASS")
    else:
        print(f"FAIL - Got '{result}' but expected '{expected}'")
