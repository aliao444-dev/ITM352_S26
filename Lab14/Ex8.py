# Exercise 8 - Heatmap of pickup vs dropoff community area

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

data_file = Path(__file__).parent / "taxi trips Fri 7_7_2017.csv"
df = pd.read_csv(data_file)
df = df.dropna(subset=['pickup_community_area', 'dropoff_community_area'])

# Count trips between each pickup/dropoff area pair
heatmap_data = df.groupby(['pickup_community_area', 'dropoff_community_area']).size().unstack(fill_value=0)

plt.figure(figsize=(14, 10))
sns.heatmap(heatmap_data, cmap='YlOrRd', linewidths=0)
plt.title('Trip Frequency: Pickup vs Dropoff Community Area — Fri 7/7/2017')
plt.xlabel('Dropoff Community Area')
plt.ylabel('Pickup Community Area')
# Note: each axis number = a Chicago community area ID
plt.tight_layout()
plt.show()
