import csv
import os

filename = "Employee_data.csv"
salaries = []

if os.path.exists(filename):

    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        # Skip the header row
        headers=next(reader)
        # Collects all the salaries while reading through the file
        salary_index = headers.index("Annual_Salary")

        # Process each row in the CSV
        print(headers)
        for row in reader:
            print(row)
            # Create a new column for the salary after tax
            salaries.append(float(row[salary_index]))

print(salaries)
if (salaries):
    average_salary = sum(salaries) / len(salaries)
    print(f"Average Salary: {average_salary:.2f}")
    max_salary = max(salaries)
    print(f"Maximum Salary: {max_salary:.2f}")
    min_salary = min(salaries)
    print(f"Minimum Salary: {min_salary:.2f}")
else:
    print("No salary data found.")