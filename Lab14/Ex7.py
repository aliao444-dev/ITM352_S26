# Exercise 7 - 3D scatter plot of fares, trip miles, and dropoff area

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pathlib import Path

data_file = Path(__file__).parent / "Trips from area 8.json"
df = pd.read_json(data_file)
df = df.dropna(subset=['fare', 'trip_miles', 'dropoff_community_area'])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(df['fare'], df['trip_miles'], df['dropoff_community_area'], alpha=0.2, s=5)

ax.set_xlabel('Fare ($)')
ax.set_ylabel('Trip Miles')
ax.set_zlabel('Dropoff Community Area')
ax.set_title('Fares, Trip Miles, and Dropoff Area — Area 8')
plt.show()
