# Exercise 5d - Conclusions from fare vs trip miles scatter

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

data_file = Path(__file__).parent / "Trips from area 8.json"
df = pd.read_json(data_file)
df = df.dropna(subset=['fare', 'trip_miles'])

plt.plot(df['fare'], df['trip_miles'], linestyle="none", marker="v", color="cyan", alpha=0.2)
plt.xlabel('Fare ($)')
plt.ylabel('Trip Miles')
plt.title('Fare vs Trip Miles — Area 8')
plt.show()

# Conclusions:
# 1. Strong positive correlation — longer trips cost more, as expected.
# 2. Outliers exist: high fares with few miles (possible wait time or surcharges).
# 3. Several trips cluster near $0 fare / 0 miles — likely errors or cancelled trips.
