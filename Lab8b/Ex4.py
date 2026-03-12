# Access a specific element from a list based on its index
def get_element(input_list, index):
    return input_list[index]

# Define a list with 5 elements (indices 0 through 4)
my_list = [1, 2, 3, 4, 5]

# Retrieve items using valid zero-based indices
print(get_element(my_list, 1)) # Returns the second item (2)
print(get_element(my_list, 4)) # Returns the fifth item (5)