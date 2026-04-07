# Read in a file from a URL and save a local CSV file with the first 10 rows

from fileinput import filename
import time
from pathlib import Path

import pandas as pd
import numpy as np
import pyarrow

from Assignment2.assignment2 import display_initial_rows, exit_program

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
        
def defisplay_initial_rows():
    print("Enter rowws to display:")
    print(f" - Enter a number 1 to (len)(dataframe)")
    print(" - Enter 'all' to display all rows")
    print(" - to skip preview")


# Call load_csv to load the data and print the first 10 rows
# filename = 'https://drive.google.com/uc?id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA&export=download'
#filename = "sales_data_test.csv"
sales_data = load_csv(filename)


def main():
    while True:
        print("Sales Data Dashboard")
        display_initial_rows()
def display_menu(dataframe):
    menu_options = (
        ("Show the first n rows of sales data", show_first_n_rows),
        ("Show the number of employees by region", show_employees_by_region),
        ("Exit", exit_program)
    )




def display_menu(dataframe):
    menu_options = (
        ("Show the first n rows of sales data", show_first_n_rows),
        ("Show the number of employees by region", show_employees_by_region),
        ("Exit", exit_program)
    )

    print("Available options:")
    for i, (option_text, _) in enumerate(menu_options, start=1):
        print(f"{i}. {option_text}")

    try:
        menu_len = len(menu_options)
        choice = int(input(f"Enter the number of your choice (1-{menu_len}
        if i <= choice <= menu_len:
            _, action = menu_options[choice - 1]
            action(dataframe)
        else:
            print("Invalid choice. Please select a valid option.")


# Call load_csv to load the data and print the first 10 rows
# filename = 'https://drive.google.com/uc?id=1Fv_vhoN
filename = "sales_data_test.csv"
sales_data = load_csv(filename)


# Run the main processing loop
if __name__ == "__main__":
    main()