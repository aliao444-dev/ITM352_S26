#Read a CSV file and create a data frame
# Print some useful info
# Pivot the data frame, aggregate the sales by region, with columns defined by order_type and totals.
import pandas as pd
import numpy as np
import pyarrow
from tabulate import tabulate

filename = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

pd.set_option('display.max_columns', None) # Show all columns

df = pd.read_csv(filename, engine="pyarrow")
df['order_date'] = pd.to_datetime(df['order_date'], format='%Y-%m-%d', errors='coerce')

# Coerce quantity and unit_price to numeric, setting errors to Null
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')
df['sales'] = df['quantity'] * df['unit_price']

pivot_table = df.pivot_table(values='sales',
                             index='sales_region',
                             columns='order_type',
                             aggfunc=np.sum,
                             margins=True,
                             margins_name='Total Sales')

print(tabulate(pivot_table, headers='keys', tablefmt='grid', floatfmt='.2f'))

print(df.head(5))
