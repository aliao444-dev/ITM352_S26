# Retrieve and analyze Chicago passenger vehicle license data from the city's open API

import pandas as pd
from sodapy import Socrata

# Socrata client connects to Chicago's open data portal (no auth needed for public datasets)
client = Socrata("data.cityofchicago.org", None)

# Fetch the first 500 records from the passenger vehicle licenses dataset (rr23-ymwb)
print("Fetching 500 records from Chicago vehicle license API...")
results = client.get("rr23-ymwb", limit=500)

# Convert the list of dicts returned by the API into a DataFrame
df = pd.DataFrame.from_records(results)

print(f"\nRows: {len(df)}  Columns: {list(df.columns)}")
print("\nFirst 5 rows:")
print(df.head())

# Print each vehicle and its fuel source
print("\n--- Vehicles and Fuel Sources ---")
for index, row in df.iterrows():
    print(f"  {row.get('vehicle_make', 'N/A')} {row.get('vehicle_model', '')} ({row.get('vehicle_model_year', 'N/A')}) — Fuel: {row.get('vehicle_fuel_source', 'N/A')}")

# Group by fuel type and count vehicles per fuel source
print("\n--- Vehicles per Fuel Source ---")
fuel_counts = df.groupby('vehicle_fuel_source').size().sort_values(ascending=False)
for fuel, count in fuel_counts.items():
    print(f"  {fuel}: {count}")
