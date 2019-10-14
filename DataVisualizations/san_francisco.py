import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Get rainfall for one month from file.
filename = 'weather-trends.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index, column in enumerate(header_row):
        print(index, column)