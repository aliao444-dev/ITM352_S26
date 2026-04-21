# Exercise 3 - Load data for payment method / tips histogram

import pandas as pd
from pathlib import Path

data_file = Path(__file__).parent / "Trips from area 8.json"
df = pd.read_json(data_file)

print(f"Loaded {len(df)} rows")
print(f"Columns: {list(df.columns)}")
