# Read interest rate data from the US Treasury website using pandas read_html()
# Print columns and loop through rows to print 1-month rates

import ssl
import pandas as pd


url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202603"

# Open the URL andu se read_html() to parse tables from the page. 
ssl._create_default_https_context = ssl._create_unverified_context

print(f"Opening URL: {url}")

# read_html() returns a list of all tables found on the page
tables = pd.read_html(url)
df = tables[0]  # The interest rate table is the first table

print(f"\nColumns: {list(df.columns)}")

# Loop through rows and print the date and 1-month rate
print("\n1 Month Interest Rates:")
for index, row in df.iterrows():
    print(f"  {row['Date']}: {row['1 Mo']}")