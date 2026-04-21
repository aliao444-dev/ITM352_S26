# Exercise 4 - Load Trips_Fri07072017T4 trip_miles gt1.json

import pandas as pd
from pathlib import Path

data_file = Path(__file__).parent / "Trips_Fri07072017T4 trip_miles gt1.json"
df = pd.read_json(data_file)

print(f"Loaded {len(df)} rows")
print(f"Columns: {list(df.columns)}")
