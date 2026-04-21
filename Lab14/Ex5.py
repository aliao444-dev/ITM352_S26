# Exercise 5 - Load Trips from area 8.json for fare vs trip miles scatter plots

import pandas as pd
from pathlib import Path

data_file = Path(__file__).parent / "Trips from area 8.json"
df = pd.read_json(data_file)

print(f"Loaded {len(df)} rows")
print(f"Columns: {list(df.columns)}")
