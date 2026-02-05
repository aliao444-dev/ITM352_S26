# To answer 3 we can do the same as we did in Ex2c.py but with a list of dictionaries

responses = [5, 7, 3, 8]
respondent_ids = (1012, 1035, 1021, 1053)

survey_dict = dict(zip(respondent_ids, responses))
# Zips together the respondent_ids and responses into a dictionary where the keys are respondent_ids and the values are responses
print("Survey responses with respondent IDs:", survey_dict)

print(f"Respondent {respondent_ids[2]} gave a response of {survey_dict[respondent_ids[2]]}")
