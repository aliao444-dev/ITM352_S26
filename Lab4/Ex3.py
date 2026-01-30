# Manipulate a list in various ways
# Name: Rick Kazman
# Date: Jan 29, 2026

responseValues = [(5, 7, 3, 8)]
responseValues.append(0)
print("After appending 0:", responseValues)

# responseValues.insert(2, 6)
responseValues = responseValues[:2] + [6] + responseValues[2:]
# Colon seperates the beginning index from the ending index, 2 means up to but not including index 2
# The two lines functionally do the same thing, but the second one is more manual (slicing)
print("After inserting 6 at index 2:", responseValues)

