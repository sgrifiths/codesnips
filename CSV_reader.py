import csv
from datatime import datetime

print("---------------------------")
print(dir(csv))
print("---------------------------")
print(dir(dict))
print("---------------------------")

path = "D:\Python Applications\codesnips\gsd.csv"

file = open(path, newline='')
reader = csv.reader(file)

header = next(reader)  # the first lines is the header

data = []
for row in reader
    # row = [Date, Open, High, Low, Close, Volume, Adj. Close]
    date = datetime.strptime(row[0], '%D/%M/%Y'
    print(header)
    print(data[0])

    row = int(input('Row: '))

    print(data[row])

    print(max(data))
