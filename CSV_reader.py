import csv
from datetime import datetime
from datediff import cal_days_diff


print("---------------------------")
print(dir(csv))
print("---------------------------")
print(dir(dict))
print("---------------------------")
print(dir(datetime))

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
returns_path = "D:\Python Applications\codesnips\g_returns.csv"
file = open(returns_path, 'w')
writer = csv.writer(file)
writer.writerow(["Date", "Return"])

for i in range(len(data) - 1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]
    yesterdays_row = data[i - 1]
    yesterdays_price = yesterdays_row[-1]
    yesterdays_date = yesterdays_row[0]

    daily_return = (todays_price - yesterdays_price) / yesterdays_price
    formatted_date = todays_date.strftime('%m/%d/%Y')
    writer.writerow([formatted_date, daily_return])
    print(cal_days_diff(todays_date,yesterdays_date,'%m/%d/%Y'))
