# Define a list of survey responses (5, 7, 3, 8) and store them in a
# variable. Next define a tuple of respondent ID values (1012, 1035, 1021, and 1053).
# Use the .append() method to add a new survey response of 6 to the list.
# Name: Anthony Liao
# Date: Jan 29, 2026

# response = [5, 7, 3, 8]
# respondent_ids = (1012, 1035, 1021, 1053)
# response.append(respondent_ids)
# print("Survey responses with respondent IDs:", response)
# [5, 7, 3, 8, (1012, 1035, 1021, 1053)] gets created, its shmushed and weird

response_values = [(1012, 5), (1035, 7), (1021, 3), (1053, 8)]
response_values.sort()
print("Sorted survey responses with respondent IDs:", response_values)
