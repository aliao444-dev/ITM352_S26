# Exercise 3a - Bar chart: payment method (X) vs sum of tips (Y)

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

data_file = Path(__file__).parent / "Trips from area 8.json"
df = pd.read_json(data_file)
df['tips'] = pd.to_numeric(df['tips'], errors='coerce')

tips_by_payment = df.groupby('payment_type')['tips'].sum()

plt.bar(tips_by_payment.index, tips_by_payment.values)
plt.xlabel('Payment Method')
plt.ylabel('Sum of Tips')
plt.title('Total Tips by Payment Method (Area 8)')
plt.show()
