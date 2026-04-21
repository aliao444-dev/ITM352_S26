# Exercise 3c - Fully styled: colors, fontweight, value labels on each bar

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

data_file = Path(__file__).parent / "Trips from area 8.json"
df = pd.read_json(data_file)
df['tips'] = pd.to_numeric(df['tips'], errors='coerce')
df = df.dropna(subset=['payment_type', 'tips'])

tips_by_payment = df.groupby('payment_type')['tips'].sum()
freq_by_payment  = df.groupby('payment_type').size()

colors = ['steelblue', 'coral', 'mediumseagreen']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# --- Tips bar chart ---
bars1 = ax1.bar(tips_by_payment.index, tips_by_payment.values, color=colors, edgecolor='black')
ax1.set_title('Taxi Tips by Payment Type', fontweight='bold', fontsize=13)
ax1.set_xlabel('Payment Type', fontweight='bold')
ax1.set_ylabel('Total Tips ($)', fontweight='bold')
# Add dollar value labels on top of each bar
for bar in bars1:
    ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5,
             f'${bar.get_height():.2f}', ha='center', va='bottom', fontweight='bold')

# --- Frequency bar chart ---
bars2 = ax2.bar(freq_by_payment.index, freq_by_payment.values, color=colors, edgecolor='black')
ax2.set_title('Trip Frequency by Payment Type', fontweight='bold', fontsize=13)
ax2.set_xlabel('Payment Type', fontweight='bold')
ax2.set_ylabel('Frequency', fontweight='bold')
# Add count labels on top of each bar
for bar in bars2:
    ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 3,
             str(int(bar.get_height())), ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()
