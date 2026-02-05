country_capitals = {
    "Germany": "Berlin",
    "Canada": "Ottawa",
    "England": "London"}

print(country_capitals)
# Stop and run here ^
# Spits {'Germany': 'Berlin', 'Canada': 'Ottawa', 'England': 'London'} in Terminal


print(country_capitals["Canada"])
# Stop and run here ^ test one of the countries ("index" Canada)
print(country_capitals["England"])


country_capitals["Italy"] = "Rome"
print(country_capitals)
# Stop and run here ^ test adding a new country


country_capitals["Italy"] = "Milan"
print(country_capitals)
# Example of modifying a dictionary entry, Milan isn't Italy's capital, but shows its easy to change
# Stop and run here ^ overwrites Italy's capital to Milan

print("Germany" in country_capitals)
print("Spain" not in country_capitals)
#Stop and run here ^ test if a key is in the dictionary, should return True for Germany and True for Spain not appearing
print("Korea" in country_capitals)
#Stop and run here ^ Korea is not in the dictionary, should return False