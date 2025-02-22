import datetime

x = datetime.datetime.now()
mdays=[31,28,31,30,31,30,31,31,30,31,30,31]
weeks=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
y=int(x.strftime("%Y"))
m=int(x.strftime("%m"))
d=int(x.strftime("%d"))
# 1. Write a Python program to subtract five days from current date.
if(d-5<=0):
    if(m-1==0):
        dd=31+(d-5)
    else:
        dd=mdays[m-2]+(d-5)
else:
    dd=d-5
print(dd)
# 2. Write a Python program to print yesterday, today, tomorrow.
y=int()
t=int()
if(d-1<=0):
    if(m-1==0):
        y=31
    else:
        y=mdays[m-2]
else:
    y=d-1

if(d+1>mdays[m-1]):
    t=1
else:
    t=d+1
print(y,d,t)
w=x.strftime("%A")
yy=weeks[(weeks.index(w)-1)%7]
tt=weeks[(weeks.index(w)+1)%7]
print(yy,w,tt)
# 3. Write a Python program to drop microseconds from datetime.
st=str(x)
st=st[:st.find('.')]
print(st)
# 4. Write a Python program to calculate two date difference in seconds.
f = datetime.datetime(2020, 5, 17, 12, 13, 47)
s = datetime.datetime(2020, 5, 17, 8, 45, 32)
sumo=int(f.strftime("%H"))*3600+int(f.strftime("%M"))*60+int(f.strftime("%S"))
sums=int(s.strftime("%H"))*3600+int(s.strftime("%M"))*60+int(s.strftime("%S"))
print(abs(sumo-sums))