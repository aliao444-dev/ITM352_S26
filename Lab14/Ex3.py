# Exercise 3 - Load trips data and inspect it

import pandas as pd
from pathlib import Path

data_file = Path(__file__).parent / "Trips from area 8.json"
df = pd.read_json(data_file)
df['tips'] = pd.to_numeric(df['tips'], errors='coerce')

print(f"Loaded {len(df)} rows")
print(df[['payment_type', 'tips', 'fare', 'trip_miles']].head(10))
print("\nTips column stats:")
print(df['tips'].describe())
