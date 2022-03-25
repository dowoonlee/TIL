import sys
mint = {"January":1,
        "February":2,
        "March":3,
        "April":4,
        "May":5,
        "June":6,
        "July":7,
        "August":8,
        "September":9,
        "October":10,
        "November":11,
        "December":12}
m2d_t = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m2d_f = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date = list(map(str,sys.stdin.readline().rstrip().split(",")))
month = mint[date[0].split()[0]]
day = int(date[0].split()[1])
year = int(date[1].split()[0])
hour = int(date[1].split()[1].split(":")[0])
min = int(date[1].split()[1].split(":")[1])

def isyr(yr):
    r4, r100, r400 = yr%4, yr%100, yr%400
    if (not r4) and r100:
        return True
    elif (not r100) and (not r400):
        return True
    else:
        return False


if isyr(year):#윤년
    total = 366*24*60
    passed = (sum(m2d_t[0:month-1])+(day-1))*24*60 + hour*60+min
else:
    total = 365*24*60
    passed = (sum(m2d_f[0:month-1])+(day-1))*24*60 + hour*60+min

print(passed/total*100)




