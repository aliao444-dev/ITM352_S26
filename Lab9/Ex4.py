import os
import csv

# Dynamically construct the path to taxi_1000.csv
filename = os.path.join(os.path.dirname(__file__), "taxi_1000.csv")

num_rows = 0
valid_fares_count = 0
with open(filename) as csvfile:
    csv_reader = csv.reader(csvfile)

    total_fare = 0.0
    max_distance = 0.0

    for line in csv_reader:
        if num_rows == 0:
            fare_index = line.index("Fare")
            distance_index = line.index("Trip Miles")
            num_rows += 1
            continue

        if num_rows > 0:
            try:
                tripFare = float(line[fare_index])
                tripDistance = float(line[distance_index])

                if tripFare > 10:  # Only consider fares greater than $10
                    total_fare += tripFare
                    valid_fares_count += 1
                    if tripDistance > max_distance:
                        max_distance = tripDistance
            except ValueError:
                continue  # Skip rows with invalid data

        num_rows += 1

    if valid_fares_count > 0:
        average_fare = total_fare / valid_fares_count
        print(f"Total fares (>$10): ${total_fare:.2f}")
        print(f"Average fare (>$10): ${average_fare:.2f}")
        print(f"Maximum trip distance: {max_distance:.2f} miles")
    else:
        print("No fares greater than $10 found.")