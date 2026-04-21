# Exercise 4b - Conclusions from fare vs tips scatter plot
# (Same plot as 4a — conclusions noted below)

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

# Conclusions:
# 1. There is a positive correlation — higher fares generally produce higher tips.
# 2. A large cluster of trips have $0 tips, likely cash tips not captured in the data.
# 3. Most tips fall between 15-20% of the fare for those who do tip electronically.
