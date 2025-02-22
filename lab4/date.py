import datetime

x = datetime.datetime.now()
x = datetime.datetime(2018, 6, 1)
print(int(x.strftime("%d"))-5)