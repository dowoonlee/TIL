import sys

tday = list(map(int, sys.stdin.readline().split()))

dday = list(map(int, sys.stdin.readline().split()))

def ycheck(yr):
    res=False
    if yr%4==0:
        res=True
    if yr%100==0:
        res=False
    if yr%400==0:
        res=True
    return res

m1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def y2d(ymd):
    if ycheck(ymd[0]):#윤년
        days = sum(m2[0:ymd[1]-1])+ymd[2]
    else:
        days = sum(m1[0:ymd[1]-1])+ymd[2]
    return days

#check



if dday[0]>=tday[0]+1000 and y2d(dday)>=y2d(tday):
    print('gg')
else:
    ans = 0
    for yr in range(tday[0], dday[0]):
        if ycheck(yr):
            ans+=366
        else:
            ans+=365
    ans-=y2d(tday)
    ans+=y2d(dday)
    print('D-%d'%ans)
