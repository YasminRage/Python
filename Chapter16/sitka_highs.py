from pathlib import Path
import csv

path = Path('weather_data.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

# ['STATION', 'NAME', 'DATE', 'TAVG', 'TMAX', 'TMIN']


for index, column_header in enumerate(header_row):
    print(index, column_header)

#0 STATION
# 1 NAME
# 2 DATE
# 3 TAVG
# 4 TMAX
# 5 TMIN