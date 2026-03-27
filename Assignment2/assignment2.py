"""
Assignment 2: Sales Dashboard
ITM 352 - Spring 2026
Author: Anthony
Description: Interactive CLI sales dashboard that loads sales_data.csv
             and provides pivot table analytics.
"""

import pandas as pd
import time
import os
import sys

# ─────────────────────────────────────────────
# R1 – Data Loading
# ─────────────────────────────────────────────

def load_data(filepath="sales_data.csv"):
    """
    Load sales data from CSV file.
    - Times the load operation
    - Reports row count and column names
    - Replaces missing values with 'N/A' (str) or 0 (numeric)
    - Validates required columns exist
    Returns a DataFrame, or None on failure.
    """
    required_columns = {
        "order_number", "employee_id", "employee_name", "job_title",
        "sales_region", "order_date", "order_type", "customer_type",
        "customer_name", "customer_state", "product_category",
        "product_number", "produce_name", "quantity", "unit_price"
    }

    if not os.path.isfile(filepath):
        print(f"[ERROR] File not found: {filepath}")
        return None

    print(f"\nLoading data from '{filepath}' ...")
    start = time.time()
    try:
        df = pd.read_csv(filepath)
    except Exception as e:
        print(f"[ERROR] Could not read file: {e}")
        return None
    elapsed = time.time() - start

    # Validate columns
    missing_cols = required_columns - set(df.columns)
    if missing_cols:
        print(f"[ERROR] Missing required columns: {missing_cols}")
        return None

    # Handle missing data
    for col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].fillna("N/A")
        else:
            df[col] = df[col].fillna(0)

    # Ensure numeric types for quantity and unit_price
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce").fillna(0)
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce").fillna(0)

    # Derived column used by several analytics
    df["total_sales"] = df["quantity"] * df["unit_price"]

    print(f"  Loaded {len(df):,} rows in {elapsed:.3f} seconds.")
    print(f"  Columns ({len(df.columns)}): {', '.join(df.columns.tolist())}")
    return df


# ─────────────────────────────────────────────
# R3 – Predefined Analytics (8 tasks)
# ─────────────────────────────────────────────

def task1_total_sales_by_region(df):
    """Total sales (quantity * unit_price) by sales region."""
    pt = df.pivot_table(
        values="total_sales",
        index="sales_region",
        aggfunc="sum"
    ).rename(columns={"total_sales": "Total Sales ($)"})
    print("\n[Task 1] Total Sales by Region")
    print(pt["Total Sales ($)"].map("${:,.2f}".format).to_frame().to_string())
    _export_prompt(pt, "task1_total_sales_by_region")


def task2_avg_sales_by_product(df):
    """Average order value by product category."""
    pt = df.pivot_table(
        values="total_sales",
        index="product_category",
        aggfunc="mean"
    ).rename(columns={"total_sales": "Avg Order Value ($)"})
    print("\n[Task 2] Average Sales by Product Category")
    print(pt["Avg Order Value ($)"].map("${:,.2f}".format).to_frame().to_string())
    _export_prompt(pt, "task2_avg_sales_by_product")


def task3_total_quantity_by_region_product(df):
    """Total quantity sold, broken down by region and product category."""
    pt = df.pivot_table(
        values="quantity",
        index="sales_region",
        columns="product_category",
        aggfunc="sum",
        fill_value=0
    )
    print("\n[Task 3] Total Quantity Sold by Region and Product Category")
    print(pt.to_string())
    _export_prompt(pt, "task3_quantity_region_product")


def task4_sales_by_order_type(df):
    """Total sales split by order type (Retail vs Wholesale)."""
    pt = df.pivot_table(
        values="total_sales",
        index="order_type",
        aggfunc="sum"
    ).rename(columns={"total_sales": "Total Sales ($)"})
    print("\n[Task 4] Total Sales by Order Type")
    print(pt["Total Sales ($)"].map("${:,.2f}".format).to_frame().to_string())
    _export_prompt(pt, "task4_sales_by_order_type")


def task5_max_min_sales_by_employee(df):
    """Maximum and minimum individual order value per employee."""
    pt = df.pivot_table(
        values="total_sales",
        index="employee_name",
        aggfunc=["max", "min"]
    )
    pt.columns = ["Max Order ($)", "Min Order ($)"]
    print("\n[Task 5] Max and Min Order Value by Employee")
    display = pt.copy()
    display["Max Order ($)"] = display["Max Order ($)"].map("${:,.2f}".format)
    display["Min Order ($)"] = display["Min Order ($)"].map("${:,.2f}".format)
    print(display.to_string())
    _export_prompt(pt, "task5_max_min_by_employee")


def task6_sales_by_customer_type(df):
    """Total sales by customer type (Individual vs Business)."""
    pt = df.pivot_table(
        values="total_sales",
        index="customer_type",
        aggfunc="sum"
    ).rename(columns={"total_sales": "Total Sales ($)"})
    print("\n[Task 6] Total Sales by Customer Type")
    print(pt["Total Sales ($)"].map("${:,.2f}".format).to_frame().to_string())
    _export_prompt(pt, "task6_sales_by_customer_type")


def task7_unique_customers_by_region(df):
    """Number of unique customers per sales region."""
    pt = df.pivot_table(
        values="customer_name",
        index="sales_region",
        aggfunc=pd.Series.nunique
    ).rename(columns={"customer_name": "Unique Customers"})
    print("\n[Task 7] Unique Customers by Region")
    print(pt.to_string())
    _export_prompt(pt, "task7_unique_customers_by_region")


def task8_total_sales_by_state(df):
    """Total sales by customer state."""
    pt = df.pivot_table(
        values="total_sales",
        index="customer_state",
        aggfunc="sum"
    ).rename(columns={"total_sales": "Total Sales ($)"})
    pt.sort_values("Total Sales ($)", ascending=False, inplace=True)
    print("\n[Task 8] Total Sales by Customer State (descending)")
    print(pt["Total Sales ($)"].map("${:,.2f}".format).to_frame().to_string())
    _export_prompt(pt, "task8_sales_by_state")


# ─────────────────────────────────────────────
# R4 – Custom Pivot Table Generator
# ─────────────────────────────────────────────

AGGFUNC_MAP = {
    "1": ("sum",    "Sum"),
    "2": ("mean",   "Mean (Average)"),
    "3": ("count",  "Count"),
    "4": ("max",    "Max"),
    "5": ("min",    "Min"),
    "6": ("median", "Median"),
}


def task9_custom_pivot(df):
    """
    Interactively build a custom pivot table.
    The user selects:
      - rows (index)
      - columns (optional)
      - value field
      - aggregation function
    """
    categorical_cols = [c for c in df.columns if df[c].dtype == object]
    numeric_cols     = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]

    print("\n[Task 9] Custom Pivot Table Generator")

    # ---- select rows ----
    print("\nAvailable categorical columns for ROWS:")
    for i, col in enumerate(categorical_cols, 1):
        print(f"  {i}. {col}")
    row_col = _pick_column(categorical_cols, "Select row column number: ")
    if row_col is None:
        return

    # ---- select columns (optional) ----
    print("\nAvailable categorical columns for COLUMNS (or 0 to skip):")
    for i, col in enumerate(categorical_cols, 1):
        print(f"  {i}. {col}")
    print("  0. None / Skip")
    col_col = _pick_column(categorical_cols, "Select column column number (0 to skip): ", allow_skip=True)

    # ---- select value ----
    print("\nAvailable numeric columns for VALUES:")
    for i, col in enumerate(numeric_cols, 1):
        print(f"  {i}. {col}")
    val_col = _pick_column(numeric_cols, "Select value column number: ")
    if val_col is None:
        return

    # ---- select aggregation ----
    print("\nAggregation functions:")
    for key, (_, label) in AGGFUNC_MAP.items():
        print(f"  {key}. {label}")
    while True:
        agg_choice = input("Select aggregation function number: ").strip()
        if agg_choice in AGGFUNC_MAP:
            aggfunc, agg_label = AGGFUNC_MAP[agg_choice]
            break
        print("  [!] Invalid choice. Please enter a number from the list.")

    # ---- build pivot ----
    try:
        if col_col:
            pt = df.pivot_table(
                values=val_col,
                index=row_col,
                columns=col_col,
                aggfunc=aggfunc,
                fill_value=0
            )
        else:
            pt = df.pivot_table(
                values=val_col,
                index=row_col,
                aggfunc=aggfunc
            )
    except Exception as e:
        print(f"  [ERROR] Could not create pivot table: {e}")
        return

    title = f"{agg_label} of '{val_col}' by '{row_col}'"
    if col_col:
        title += f" / '{col_col}'"
    print(f"\n{title}")
    print(pt.to_string())
    _export_prompt(pt, "custom_pivot")


# ─────────────────────────────────────────────
# Helper utilities
# ─────────────────────────────────────────────

def _pick_column(col_list, prompt, allow_skip=False):
    """
    Prompt the user to choose a column by number from col_list.
    Returns the column name, None (for "none/skip" if allow_skip=True),
    or None on invalid input after a warning.
    """
    while True:
        raw = input(prompt).strip()
        if allow_skip and raw == "0":
            return None
        if raw.isdigit():
            idx = int(raw) - 1
            if 0 <= idx < len(col_list):
                return col_list[idx]
        print(f"  [!] Please enter a number between {'0 and' if allow_skip else '1 and'} {len(col_list)}.")


def _export_prompt(pt, default_name):
    """
    Ask the user whether to export the pivot table to an Excel file.
    """
    choice = input("\nExport this table to Excel? (y/n): ").strip().lower()
    if choice != "y":
        return
    filename = input(f"  Enter filename (default: {default_name}.xlsx): ").strip()
    if not filename:
        filename = f"{default_name}.xlsx"
    if not filename.endswith(".xlsx"):
        filename += ".xlsx"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)
    try:
        pt.to_excel(filepath)
        print(f"  Saved to '{filepath}'.")
    except Exception as e:
        print(f"  [ERROR] Could not save file: {e}")


# ─────────────────────────────────────────────
# R2 – Main Menu
# ─────────────────────────────────────────────

# Menu items: (display label, function that accepts df)
MENU = (
    ("Total Sales by Region",                          task1_total_sales_by_region),
    ("Average Sales by Product Category",              task2_avg_sales_by_product),
    ("Total Quantity by Region and Product Category",  task3_total_quantity_by_region_product),
    ("Total Sales by Order Type",                      task4_sales_by_order_type),
    ("Max and Min Sales by Employee",                  task5_max_min_sales_by_employee),
    ("Total Sales by Customer Type",                   task6_sales_by_customer_type),
    ("Unique Customers by Region",                     task7_unique_customers_by_region),
    ("Total Sales by Customer State",                  task8_total_sales_by_state),
    ("Custom Pivot Table Generator",                   task9_custom_pivot),
    ("Exit",                                           None),
)


def print_menu():
    """Display the numbered main menu."""
    print("\n" + "=" * 50)
    print("       Sales Dashboard – Main Menu")
    print("=" * 50)
    for i, (label, _) in enumerate(MENU, 1):
        print(f"  {i:2}. {label}")
    print("=" * 50)


def run_menu(df):
    """
    Loop: show menu, read choice, call corresponding function.
    Validates that input is an integer in [1, len(MENU)].
    """
    while True:
        print_menu()
        raw = input("Enter choice: ").strip()

        if not raw.isdigit():
            print("  [!] Please enter a number.")
            continue

        choice = int(raw)
        if not (1 <= choice <= len(MENU)):
            print(f"  [!] Please enter a number between 1 and {len(MENU)}.")
            continue

        label, func = MENU[choice - 1]

        if func is None:
            print("\nGoodbye!")
            sys.exit(0)

        func(df)


# ─────────────────────────────────────────────
# Entry Point
# ─────────────────────────────────────────────

def main():
    print("=" * 50)
    print("   ITM 352 – Assignment 2: Sales Dashboard")
    print("=" * 50)

    # Accept optional filepath argument from command line
    script_dir = os.path.dirname(os.path.abspath(__file__))
    default_csv = os.path.join(script_dir, "sales_data.csv")
    filepath = sys.argv[1] if len(sys.argv) > 1 else default_csv

    df = load_data(filepath)
    if df is None:
        print("[FATAL] Data could not be loaded. Exiting.")
        sys.exit(1)

    run_menu(df)


if __name__ == "__main__":
    main()
