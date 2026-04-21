# Exercise 4a - Scatter plot: fare (X) vs tips (Y)

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

data_file = Path(__file__).parent / "Trips_Fri07072017T4 trip_miles gt1.json"
df = pd.read_json(data_file)
df['fare'] = pd.to_numeric(df['fare'], errors='coerce')
df['tips'] = pd.to_numeric(df['tips'], errors='coerce')
df = df.dropna(subset=['fare', 'tips'])

plt.scatter(df['fare'], df['tips'], alpha=0.3, s=10)
plt.xlabel('Fare ($)')
plt.ylabel('Tips ($)')
plt.title('Fares vs Tips — Friday 07/07/2017 (trips > 1 mile)')
plt.show()

# Conclusion: Tips tend to increase with fare, but many trips have $0 tip
# regardless of fare amount, suggesting cash tips not recorded or optional tipping.
