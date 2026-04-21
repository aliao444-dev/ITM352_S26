# Exercise 6b - Filter out trips of 0 miles

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

data_file = Path(__file__).parent / "Trips from area 8.json"
df = pd.read_json(data_file)
df = df.dropna(subset=['fare', 'trip_miles'])
df = df[df['trip_miles'] > 0]

plt.scatter(df['fare'], df['trip_miles'], alpha=0.3, s=10)
plt.xlabel('Fare ($)')
plt.ylabel('Trip Miles')
plt.title('Fare vs Trip Miles — Area 8 (no 0-mile trips)')
plt.savefig(Path(__file__).parent / "FaresXmiles.png")
print("Saved to FaresXmiles.png")
