# Exercise 3a - Sum tips by payment type and create a basic bar chart

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

data_file = Path(__file__).parent / "Trips from area 8.json"
df = pd.read_json(data_file)
df['tips'] = pd.to_numeric(df['tips'], errors='coerce')

# Sum the tips grouped by payment type
tips_by_payment = df.groupby('payment_type')['tips'].sum()
print(tips_by_payment)

plt.bar(tips_by_payment.index, tips_by_payment.values)
plt.title('Taxi Tips by Payment Type')
plt.xlabel('Payment Type')
plt.ylabel('Total Tips ($)')
plt.show()
