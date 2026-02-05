# Store both the tuple and the list as values in a dictionary called trips
# Name: Anthony Liao
# Date: Feb 5, 2026

trip_durations = [1.1, 0.8, 2.5, 2.6]
trip_fares = [6.25, 5.25, 10.50, 8.95]

taxiTrips = {
    "miles": trip_durations,
    "fares": trip_fares
}

print(taxiTrips)

print(f"The third trip was {taxiTrips['miles'][2]} miles long.")
print(f"The fare for the third trip was ${taxiTrips['fares'][2]:.2f}.")