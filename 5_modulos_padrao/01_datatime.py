from datetime import datetime, timedelta

data = datetime(2020, 12, 1)
data_str = datetime.strptime("01/12/2003", "%d/%m/%Y")

print(data)
print(data.strftime("%d/%m/%Y"))
print(data_str)
