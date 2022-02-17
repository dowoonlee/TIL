import sys

def ycheck(yr):
    res=False
    if yr%4==0:
        res=True
    if yr%100==0:
        res=False
    if yr%400==0:
        res=True
    return res

m1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]#평년
m2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]#윤년

def y2d(ymd):
    if ycheck(ymd[0]):#윤년
        days = sum(m2[0:ymd[1]-1])+ymd[2]
    else:
        days = sum(m1[0:ymd[1]-1])+ymd[2]
    return days-1

print(y2d([2008, 1, 31]))