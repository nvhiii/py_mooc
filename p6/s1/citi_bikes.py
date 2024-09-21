# In this exercise we will write some functions for working on a file containing location data from the stations for city bikes in Helsinki.

# Each file will follow this format:

# Longitude;Latitude;FID;name;total_slot;operative;id
# 24.950292890004903;60.155444793742276;1;Kaivopuisto;30;Yes;001
# 24.956347471358754;60.160959093887129;2;Laivasillankatu;12;Yes;002
# 24.944927399779715;60.158189199971673;3;Kapteeninpuistikko;16;Yes;003

# Each station has a single line in the file. The line contains the coordinates, name, and other identifying information for the station.

# Distance between stations
# First, write a function named get_station_data(filename: str). This function should read the names and locations of all the stations in the file, and return them in a dictionary with the following format:

# {
#   "Kaivopuisto": (24.950292890004903, 60.155444793742276),
#   "Laivasillankatu": (24.956347471358754, 60.160959093887129),
#   "Kapteeninpuistikko": (24.944927399779715, 60.158189199971673)
# }

# Dictionary keys are the names of the stations, and the value attached is a tuple containing the location coordinates of the station. The first element in the tuple is the Longitude field, and the second is the Latitude field.

# Next, write a function named distance(stations: dict, station1: str, station2: str), which returns the distance between the two stations given as arguments.

# The distance is calculated using the Pythagorean theorem. The multiplication factors below are approximate values for converting latitudes and longitudes to distances in kilometres in the Helsinki region.
    
# # we will need the function sqrt from the math module 
# import math

# x_km = (longitude1 - longitude2) * 55.26
# y_km = (latitude1 - latitude2) * 111.2
# distance_km = math.sqrt(x_km**2 + y_km**2)

# Some examples of the function in action:

# stations = get_station_data('stations1.csv')
# d = distance(stations, "Designmuseo", "Hietalahdentori")
# print(d)
# d = distance(stations, "Viiskulma", "Kaivopuisto")
# print(d)

# 0.9032737292463177
# 0.7753594392019532

# NB: If Visual Studio can't find the file and you have checked that there are no spelling errors, take a look at these instructions.

# The greatest distance
# Please write a function named greatest_distance(stations: dict), which works out the two stations on the list with the greatest distance from each other. The function should return a tuple, where the first two elements are the names of the two stations, and the third element is the distance between the two.

# stations = get_station_data('stations1.csv')
# station1, station2, greatest = greatest_distance(stations)
# print(station1, station2, greatest)

# Laivasillankatu Hietalahdentori 1.478708873076181

import math

def get_station_data(filename: str):
    stations = {}
    with open(filename) as new_file:
        for line in new_file:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "Longitude":
                continue  # skip first row of headers
            stations_name = parts[3]
            longitude = float(parts[0])
            latitude = float(parts[1])
            stations[stations_name] = (longitude, latitude)

    return stations

def distance(stations: dict, station1: str, station2: str):
    x_km = (stations[station1][0] - stations[station2][0]) * 55.26
    y_km = (stations[station1][1] - stations[station2][1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    max_distance = 0
    station_pair = ("", "")  # to store the two stations with the max distance

    # Compare each station with every other station
    for station1 in stations:
        for station2 in stations:
            if station1 != station2:  # Only compare different stations
                dist = distance(stations, station1, station2)
                if dist > max_distance:
                    max_distance = dist
                    station_pair = (station1, station2)
    
    return station_pair[0], station_pair[1], max_distance
