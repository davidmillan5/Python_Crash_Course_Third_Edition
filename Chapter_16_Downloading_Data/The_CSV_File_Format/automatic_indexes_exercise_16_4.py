from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)
#print(header_row)

# Find the index of the 'name' column
name_index = header_row.index('NAME')

# Get the first data row
first_row = next(reader)
location_name = first_row[name_index]
print(first_row[name_index])

def index_finder(column_name):
    """Function in charge of finding the index of an specific column using the column name"""
    column_index = None
    for index, column_header in enumerate(header_row):
        if column_header.lower() == column_name.lower():
            column_index = index
    return column_index

#index = index_finder("TMAX")
#print(index)


# extract dates and high temperatures.
dates, highs = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    index_high_temperature = index_finder("TMAX")
    high = int(row[index_high_temperature])
    dates.append(current_date)
    highs.append(high)


# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates,highs, color='red')

# Format plot.

title = f"Daily High Temperatures, 2001\n {location_name} station."
ax.set_title(title, fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()