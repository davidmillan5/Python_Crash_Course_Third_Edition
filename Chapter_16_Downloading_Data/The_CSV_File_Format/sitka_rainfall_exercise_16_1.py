from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_full.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)


# extract dates and high temperatures.
dates, drfs = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    drf = float(row[5])
    dates.append(current_date)
    drfs.append(drf)


# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates,drfs, color='blue')

# Format plot.
ax.set_title("Daily Rainfall Amount, 2021\nSitka, AK", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Amount in mm", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()