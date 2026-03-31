#Read a CSV file and create a data frame
# Print some useful info
import pandas as pd
import pyarrow

filename = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

pd.set_option('display.max_columns', None) # Show all columns

df = pd.read_csv(filename, engine="pyarrow")
df['order_date'] = pd.to_datetime(df['order_date'], format='%Y-%m-%d', errors='coerce')

# Coerce quantity and unit_price to numeric, setting errors to Null
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')

print(df.info())
print(df.describe())
print(df.head(5))
