# Exercise 3c - Full histogram with labels and title

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

data_file = Path(__file__).parent / "Trips from area 8.json"
df = pd.read_json(data_file)
df['tips'] = pd.to_numeric(df['tips'], errors='coerce')

df = df.dropna(subset=['payment_type', 'tips'])

tips_by_payment = df.groupby('payment_type')['tips'].sum()

plt.bar(tips_by_payment.index, tips_by_payment.values, color='steelblue', edgecolor='black')
plt.xlabel('Payment Method')
plt.ylabel('Sum of Tips ($)')
plt.title('Total Tips by Payment Method — Area 8 Trips')
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()
