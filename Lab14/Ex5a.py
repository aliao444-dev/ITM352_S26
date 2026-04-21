# Exercise 5a - Scatter plot: fare (X) vs trip miles (Y) using plt.scatter()

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

data_file = Path(__file__).parent / "Trips from area 8.json"
df = pd.read_json(data_file)
df['fare'] = pd.to_numeric(df['fare'], errors='coerce')
df['trip_miles'] = pd.to_numeric(df['trip_miles'], errors='coerce')
df = df.dropna(subset=['fare', 'trip_miles'])

plt.scatter(df['fare'], df['trip_miles'])
plt.xlabel('Fare ($)')
plt.ylabel('Trip Miles')
plt.title('Fare vs Trip Miles — Area 8')
plt.show()
