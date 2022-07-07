from datetime import datetime

now = datetime.now()
# print(now.timestamp())

year = now.year
month = now.month
day = now.day

for i in range(-1, 10):
    last_day = datetime(year, month, (day-i))
    print(last_day)
