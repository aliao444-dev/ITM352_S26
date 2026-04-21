# Exercise 3b - Drop NA rows, then show tips AND frequency side by side

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

data_file = Path(__file__).parent / "Trips from area 8.json"
df = pd.read_json(data_file)
df['tips'] = pd.to_numeric(df['tips'], errors='coerce')

# Drop rows with missing payment_type or tips
df = df.dropna(subset=['payment_type', 'tips'])

tips_by_payment = df.groupby('payment_type')['tips'].sum()
freq_by_payment = df.groupby('payment_type').size()

# Two subplots: tips sum (left) and trip count/frequency (right)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

ax1.bar(tips_by_payment.index, tips_by_payment.values)
ax1.set_title('Taxi Tips by Payment Type')
ax1.set_xlabel('Payment Type')
ax1.set_ylabel('Total Tips ($)')

ax2.bar(freq_by_payment.index, freq_by_payment.values)
ax2.set_title('Trip Frequency by Payment Type')
ax2.set_xlabel('Payment Type')
ax2.set_ylabel('Frequency')

plt.tight_layout()
plt.show()
