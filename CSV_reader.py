import csv
from datetime import datetime

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
for row in reader:
    # row = [Date, Open, High, Low, Close, Volume, Adj. Close]
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1])
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])

    data.append([date, open_price, high, low, close, volume, adj_close])

# calculate and output stock value csv
returns_path = "D:\Python Applications\g_returns.csv
file = open(returns_path, 'w')
writer = csv.writer(file)
writer.writerow(["Date", "Return"])

for i in range(len(data) - 1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]
