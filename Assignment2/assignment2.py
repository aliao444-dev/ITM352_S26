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

    REQUIRED_COLUMNS = {
        "order_number", "employee_id", "employee_name", "job_title",
        "sales_region", "order_date", "order_type", "customer_type",
        "customer_name", "customer_state", "product_category",
        "product_number", "produce_name", "quantity", "unit_price"
    }


    def load_csv(filepath):
        """
        Load sales data from a CSV file using the pyarrow backend.
        - Times the load operation and reports row count / column names
        - Skips bad rows
        - Converts order_date to datetime
        - Warns (does not abort) if required columns are missing
        Returns a DataFrame, or None on failure.
        """
        if not os.path.isfile(filepath):
            print(f"[ERROR] File not found: {filepath}")
            return None

        print(f"\nLoading data from '{filepath}' ...")
        start = time.time()
        try:
            df = pd.read_csv(filepath, engine="pyarrow", on_bad_lines="skip")
        except Exception as e:
            print(f"[ERROR] Could not read file: {e}")
            return None
        elapsed = time.time() - start

        print(f"  Loaded {len(df):,} rows in {elapsed:.3f} seconds.")
        print(f"  Columns ({len(df.columns)}): {', '.join(df.columns.tolist())}")

        # Warn about missing columns but continue
        missing_cols = REQUIRED_COLUMNS - set(df.columns)
        if missing_cols:
            print(f"[WARNING] Missing columns: {', '.join(sorted(missing_cols))}")
            print("  Some analytics will not function without these fields.")

        # Convert order_date to datetime
        if "order_date" in df.columns:
            df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

        # Ensure numeric types for calculated fields
        for col in ("quantity", "unit_price"):
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

        # Derived column used by several analytics
        if "quantity" in df.columns and "unit_price" in df.columns:
            df["total_sales"] = df["quantity"] * df["unit_price"]

        return df


    # ─────────────────────────────────────────────
    # R2 – Display Initial Rows
    # ─────────────────────────────────────────────

    def display_initial_rows(data):
        """
        Prompt the user to specify how many initial rows to display.
        Accepts: a number, 'all', or empty input to skip.
        """
        while True:
            raw = input(
                "\nHow many initial rows would you like to see? "
                "(number / 'all' / Enter to skip): "
            ).strip()
            if raw == "":
                return
            if raw.lower() == "all":
                print(data.to_string())
                return
            if raw.isdigit() and int(raw) > 0:
                print(data.head(int(raw)).to_string())
                return
            print("  [!] Invalid input. Enter a positive number, 'all', or press Enter to skip.")


    # ─────────────────────────────────────────────
    # R3 – Predefined Analytics
    # ─────────────────────────────────────────────

    def show_employees_by_region(data):
        """Number of unique employees per sales region."""
        pt = data.pivot_table(
            values="employee_id",
            index="sales_region",
            aggfunc=pd.Series.nunique
        ).rename(columns={"employee_id": "Unique Employees"})
        print("\nNumber of Employees by Region")
        print(pt.to_string())
        _export_prompt(pt, "employees_by_region")


    def task1_total_sales_by_region(data):
        """Total sales (quantity * unit_price) by sales region."""
        pt = data.pivot_table(
            values="total_sales",
            index="sales_region",
            aggfunc="sum"
        ).rename(columns={"total_sales": "Total Sales ($)"})
        print("\n[1] Total Sales by Region")
        print(pt["Total Sales ($)"].map("${:,.2f}".format).to_frame().to_string())
        _export_prompt(pt, "task1_total_sales_by_region")


    def task2_avg_sales_by_product(data):
        """Average order value by product category."""
        pt = data.pivot_table(
            values="total_sales",
            index="product_category",
            aggfunc="mean"
        ).rename(columns={"total_sales": "Avg Order Value ($)"})
        print("\n[2] Average Sales by Product Category")
        print(pt["Avg Order Value ($)"].map("${:,.2f}".format).to_frame().to_string())
        _export_prompt(pt, "task2_avg_sales_by_product")


    def task3_total_quantity_by_region_product(data):
        """Total quantity sold by region and product category."""
        pt = data.pivot_table(
            values="quantity",
            index="sales_region",
            columns="product_category",
            aggfunc="sum",
            fill_value=0
        )
        print("\n[3] Total Quantity Sold by Region and Product Category")
        print(pt.to_string())
        _export_prompt(pt, "task3_quantity_region_product")


    def task4_sales_by_order_type(data):
        """Total sales split by order type (Retail vs Wholesale)."""
        pt = data.pivot_table(
            values="total_sales",
            index="order_type",
            aggfunc="sum"
        ).rename(columns={"total_sales": "Total Sales ($)"})
        print("\n[4] Total Sales by Order Type")
        print(pt["Total Sales ($)"].map("${:,.2f}".format).to_frame().to_string())
        _export_prompt(pt, "task4_sales_by_order_type")


    def task5_max_min_sales_by_employee(data):
        """Maximum and minimum individual order value per employee."""
        pt = data.pivot_table(
            values="total_sales",
            index="employee_name",
            aggfunc=["max", "min"]
        )
        pt.columns = ["Max Order ($)", "Min Order ($)"]
        print("\n[5] Max and Min Order Value by Employee")
        display = pt.copy()
        display["Max Order ($)"] = display["Max Order ($)"].map("${:,.2f}".format)
        display["Min Order ($)"] = display["Min Order ($)"].map("${:,.2f}".format)
        print(display.to_string())
        _export_prompt(pt, "task5_max_min_by_employee")


    def task6_sales_by_customer_type(data):
        """Total sales by customer type (Individual vs Business)."""
        pt = data.pivot_table(
            values="total_sales",
            index="customer_type",
            aggfunc="sum"
        ).rename(columns={"total_sales": "Total Sales ($)"})
        print("\n[6] Total Sales by Customer Type")
        print(pt["Total Sales ($)"].map("${:,.2f}".format).to_frame().to_string())
        _export_prompt(pt, "task6_sales_by_customer_type")


    def task7_unique_customers_by_region(data):
        """Number of unique customers per sales region."""
        pt = data.pivot_table(
            values="customer_name",
            index="sales_region",
            aggfunc=pd.Series.nunique
        ).rename(columns={"customer_name": "Unique Customers"})
        print("\n[7] Unique Customers by Region")
        print(pt.to_string())
        _export_prompt(pt, "task7_unique_customers_by_region")


    def task8_total_sales_by_state(data):
        """Total sales by customer state, sorted descending."""
        pt = data.pivot_table(
            values="total_sales",
            index="customer_state",
            aggfunc="sum"
        ).rename(columns={"total_sales": "Total Sales ($)"})
        pt.sort_values("Total Sales ($)", ascending=False, inplace=True)
        print("\n[8] Total Sales by Customer State (descending)")
        print(pt["Total Sales ($)"].map("${:,.2f}".format).to_frame().to_string())
        _export_prompt(pt, "task8_sales_by_state")


    # ─────────────────────────────────────────────
    # R4 – Custom Pivot Table Generator
    # ─────────────────────────────────────────────

    def get_user_selection(options, prompt):
        print(prompt)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        choice = input("Enter the number(s) of your choice(s), separated by commas: ")
        selected = [options[int(i) - 1] for i in choice.split(",")] if choice else []
        return selected


    def generate_custom_pivot_table(data):
        """Interactively build a custom pivot table."""
        print("\nCustom Pivot Table Generator")

        row_options = list(data.columns)
        col_options = row_options.copy()
        value_options = list(data.select_dtypes(include=["number"]).columns)
        agg_options = ["sum", "mean", "count"]

        rows = get_user_selection(row_options, "\nSelect rows:")
        if not rows:
            print("  [!] At least one row must be selected.")
            return

        col_options = [col for col in col_options if col not in rows]
        cols = get_user_selection(col_options, "\nSelect columns (optional, press Enter to skip):")

        values = get_user_selection(value_options, "\nSelect values:")
        if not values:
            print("  [!] At least one value must be selected.")
            return

        agg_selection = get_user_selection(agg_options, "\nSelect aggregation function:")
        agg_func = agg_selection[0] if agg_selection else "sum"

        try:
            pivot_table = pd.pivot_table(
                data,
                index=rows,
                columns=cols if cols else None,
                values=values,
                aggfunc=agg_func
            )
            print("\nCustom Pivot Table:")
            print(pivot_table.to_string())
            _export_prompt(pivot_table, "custom_pivot")
        except Exception as e:
            print(f"  [ERROR] Could not create pivot table: {e}")


    # ─────────────────────────────────────────────
    # Exit
    # ─────────────────────────────────────────────

    def exit_program(_data):
        print("\nGoodbye!")
        sys.exit(0)


    # ─────────────────────────────────────────────
    # Helper utilities
    # ─────────────────────────────────────────────

    def _export_prompt(pt, default_name):
        """Ask the user whether to export the pivot table to an Excel file."""
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
    # Menu
    # ─────────────────────────────────────────────

    menu_options = (
        ("Show the first n rows of sales data",             display_initial_rows),
        ("Show the number of employees by region",          show_employees_by_region),
        ("Total Sales by Region",                           task1_total_sales_by_region),
        ("Average Sales by Product Category",               task2_avg_sales_by_product),
        ("Total Quantity by Region and Product Category",   task3_total_quantity_by_region_product),
        ("Total Sales by Order Type",                       task4_sales_by_order_type),
        ("Max and Min Sales by Employee",                   task5_max_min_sales_by_employee),
        ("Total Sales by Customer Type",                    task6_sales_by_customer_type),
        ("Unique Customers by Region",                      task7_unique_customers_by_region),
        ("Total Sales by Customer State",                   task8_total_sales_by_state),
        ("Custom Pivot Table Generator",                    generate_custom_pivot_table),
        ("Exit the program",                                exit_program),
    )


    def display_menu():
        """Display the numbered main menu and return the user's raw input."""
        print("\n" + "=" * 50)
        print("       Sales Dashboard – Main Menu")
        print("=" * 50)
        for i, (label, _) in enumerate(menu_options, 1):
            print(f"  {i:2}. {label}")
        print("=" * 50)
        return input("Enter choice: ").strip()


    # ─────────────────────────────────────────────
    # Entry Point
    # ─────────────────────────────────────────────

    def main():
        print("=" * 50)
        print("   ITM 352 – Assignment 2: Sales Dashboard")
        print("=" * 50)

        script_dir = os.path.dirname(os.path.abspath(__file__))
        default_csv = os.path.join(script_dir, "sales_data.csv")
        filepath = sys.argv[1] if len(sys.argv) > 1 else default_csv

        data = load_csv(filepath)
        if data is None:
            print("[FATAL] Data could not be loaded. Exiting.")
            sys.exit(1)

        while True:
            choice = display_menu()

            if not choice.isdigit():
                print("  [!] Please enter a number.")
                continue

            idx = int(choice) - 1
            if not (0 <= idx < len(menu_options)):
                print(f"  [!] Please enter a number between 1 and {len(menu_options)}.")
                continue

            label, func = menu_options[idx]
            func(data)


    if __name__ == "__main__":
        main()
