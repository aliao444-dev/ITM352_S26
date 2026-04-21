# Exercise 6 - Scatter of fare vs trip miles, saved to file, filters applied

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

data_file = Path(__file__).parent / "Trips from area 8.json"
df = pd.read_json(data_file)
df = df.dropna(subset=['fare', 'trip_miles'])

plt.scatter(df['fare'], df['trip_miles'], alpha=0.3, s=10)
plt.xlabel('Fare ($)')
plt.ylabel('Trip Miles')
plt.title('Fare vs Trip Miles — Area 8')
plt.savefig(Path(__file__).parent / "FaresXmiles.png")
plt.show()
print("Saved to FaresXmiles.png")
