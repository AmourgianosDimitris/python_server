import os
import pickle
from data import Operators

class Profile:
    def __init__(self):
        self.savedir = f'data/'
        self.op = Operators()
        self.car_types = {
            'Standard Car': 'CS',
            'Big Car': 'CB',
            'Light Commercial Vehicle': 'LCV',
            'Light Commercial Vehicle': 'HCV',
            'Multi Axle Vehicle': 'MAV',
            'Two-Wheel': 'TW',
            'Auto': '3W',
            'Bus': 'B',
        }

        self.car_area = {
            'CS': 5.36,
            'CB': 8.11,
            'LCV': 6.71,
            'HCV': 15.41,
            'MAV': 27.83,
            'TW': 1.46,
            '3W': 4.16,
            'B': 25.44,
        }

        self.motor_types = {
            'Light Two-wheel': 'L1e',
            'Three wheel': 'L2e',
            'Motorcylce (heavy two wheel)': 'L3e',
            'Motorcylce with side bar': 'L4e',
            'Tricyple': 'L5e-A',
            'Commercial Tricyple': 'L5e-B',
        }

        self.motor_area = {
            'L1e': 1.5,
            'L2e': 1.5,
            'L3e': 2.1,
            'L4e': 1.8,
            'L5e-A': 2.0,
            'L5e-B': 4.0,
        }

    def append_vehicle():
        category = input("hdhdh")
        type = input("Give your request: ")
        model = input("Model: ")
        size = input("Give your request: ")
        registration_plate = input("Give your request: ")
        use = input("hhhhh")

        v = {
            'category': category,
            'type': type,
            'model': model,
            'size': size,
            'registration_plate': registration_plate,
            'use': use,
            'preference': preference
        }

        self.op.append('vehicle', v)

    def locations(self):
        name = input("Name: ")
        latitude = input("Latitude: ")
        longitude = input("Longitude: ")

        loc = {'name': name, 'Latitude': latitude, 'Longitude': longitude}
        index = self.op.load('locations')
        index[len(index)+1] = loc
        self.op.update('locations', loc)
