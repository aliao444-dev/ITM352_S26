# Use requests to query the Chicago open data API for license counts by driver type

import requests
import pandas as pd

url = "https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type"

print(f"GET {url}\n")

response = requests.get(url)

# .json() parses the response body from a JSON string into a Python list of dicts
records = response.json()

# The data is a list of dictionaries — one dict per driver_type group
print("Response format: list of dicts")
print(records)

# Convert to DataFrame and rename columns to be more readable
df = pd.DataFrame.from_records(records)
df.columns = ['driver_type', 'count']

# Set driver_type as the index so rows are labeled by type
df = df.set_index('driver_type')

print("\nLicense count by driver type:")
print(df)
