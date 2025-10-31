import datetime

date = datetime.date(2025, 10, 28)
today = datetime.date.today()

time = datetime.time(12, 00, 0)
now = datetime.datetime.now()

now = now.strftime("%d/%m/%Y %H:%M:%S")

targetDate = datetime.datetime(2024, 10, 28, 12, 30, 15)
currentDate = datetime.datetime.now()

if targetDate < currentDate:
    print("Da qua han")
else:
    print("Chua qua han")

print(now)