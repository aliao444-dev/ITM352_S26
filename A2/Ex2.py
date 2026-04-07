# Read in a file from a URL and save a local CSV file with the first 10 rows

import time
from pathlib import Path

import pandas as pd
import numpy as np
import pyarrow

pd.set_option('display.max_columns', None)


def load_csv(file_path):
    print(f"Loading file: {file_path}")
    start_time = time.time()
    try:
        df = pd.read_csv(file_path, engine="pyarrow")
        end_time = time.time()
        load_time = end_time - start_time
        print(f"File loaded successfully in {load_time:.2f} seconds.")
        print(f"Number of rows: {len(df)}")
        print(f"Columns: {list(df.columns)}")

        # Use dayfirst=True to handle mixed date formats like 9/2/19 or 15/02/2019
        df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, errors='coerce')

        # df.fillna(0, inplace=True)
        df['sales'] = df['quantity'] * df['unit_price']  # Create a new column 'sales' by multiplying 'quantity' and 'unit_price'

        required_columns = ['quantity', 'unit_price', 'order_date']
        # Check if required columns are present
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            print(f"Warning: Missing columns in the dataset: {missing_columns}")
        else:
            print("All required columns are present.")

        return df

    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        return None


def display_initial_rows():
    if sales_data is not None:
        print("First 10 rows of the sales data:")
        print(sales_data.head(10))
    else:
        print("Sales data is not available to display.")


# Call load_csv to load the data and print the first 10 rows
# filename = 'https://drive.google.com/uc?id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA&export=download'
filename = Path(__file__).parent / "sales_data_test.csv"
sales_data = load_csv(filename)


def main():
    print("Sales Data Dashboard")
    display_initial_rows()

if __name__ == "__main__":
    main()
