# Exercise 2a - Histogram of trip miles (X=trip miles, Y=frequency)

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

data_file = Path(__file__).parent / "Trips from area 8.json"
df = pd.read_json(data_file)
df['trip_miles'] = pd.to_numeric(df['trip_miles'], errors='coerce')

plt.hist(df['trip_miles'].dropna(), bins=30)
plt.xlabel('Trip Miles')
plt.ylabel('Frequency')
plt.title('Distribution of Trip Miles (Area 8)')
plt.show()
