import csv
filename = "taxi_1000.csv"
num_rows = 0
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
                total_fare += tripFare
                if tripDistance > max_distance:
                    max_distance = tripDistance
            except ValueError:
                continue  # Skip rows with invalid data

        num_rows += 1

    if num_rows > 1:
        average_fare = total_fare / (num_rows - 1)
        print(f"Total Fare: {total_fare}")
        print(f"Max Distance: {max_distance}")
        print(f"Average Fare: {average_fare}")