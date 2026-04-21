# Exercise 6c - Filter out trips less than 2 miles

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

data_file = Path(__file__).parent / "Trips from area 8.json"
df = pd.read_json(data_file)
df = df.dropna(subset=['fare', 'trip_miles'])
df = df[df['trip_miles'] >= 2]

plt.scatter(df['fare'], df['trip_miles'], alpha=0.3, s=10)
plt.xlabel('Fare ($)')
plt.ylabel('Trip Miles')
plt.title('Fare vs Trip Miles — Area 8 (trips >= 2 miles)')
plt.savefig(Path(__file__).parent / "FaresXmiles.png")
print("Saved to FaresXmiles.png")

# Anomalies noticed:
# - Some very high fares (>$50) for relatively short distances — may be wait time charges.
# - The correlation is clearer once short/zero trips are removed.
# - A few trips have unusually high mileage with low fares — possible data errors.
