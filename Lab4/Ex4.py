# Try to append to a tuple. It won't work!

survey_responses = (1012, 1035, 1021, 1053)
print("Original survey responses (tuple):", survey_responses)
# survey_responses.append(1060)  # This will cause an error, Attributeerror
survey_responses = survey_responses + (1054,)
print("After adding 1054:", survey_responses)
