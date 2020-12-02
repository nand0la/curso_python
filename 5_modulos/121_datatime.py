from datetime import datetime, timedelta

data = datetime(2020, 12, 1, 12, 10, 20)
print(data.strftime("%d/%m/%Y %H:%M:%S"))
data = data + timedelta(days=10)
print(data.strftime("%d/%m/%Y %H:%M:%S"))
