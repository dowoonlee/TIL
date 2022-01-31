import sys

w, h = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
market= []

for _ in range(n+1):
    market.append(list(map(int, sys.stdin.readline().split())))

dg = market[-1]
market = market[0:-1]

def dist(c):
    if dg[0]<=2 and c[0]<=2:#NS+NS
        if dg[0]==c[0]:#NN or SS
            d = abs(dg[1]-c[1])
        else:#NS or SN
            d = min(dg[1]+c[1], 2*w-dg[1]-c[1])+h
    elif dg[0]>2 and c[0]>2:#EW+EW
        if dg[0]==c[0]:#EE or WW
            d = abs(dg[1]-c[1])
        else:
            d = min(dg[1]+c[1], 2*h-dg[1]-c[1])+w
    else:#
        temp = [0]*5
        temp[dg[0]], temp[c[0]] = dg[1], c[1]
        if (dg[0] == 1 and c[0] == 4) or (dg[0] == 4 and c[0] == 1):#NE EN
            d = w - temp[1] + temp[4]
        elif (dg[0] == 4 and c[0] == 2) or (dg[0] == 2 and c[0] == 4):#ES SE
            d = h - temp[4] + w - temp[2]
        elif (dg[0] == 2 and c[0] == 3) or (dg[0] == 3 and c[0] == 2):#SW WS
            d = temp[2] + h - temp[3]
        else:#WN NW
            d = temp[3] + temp[1]
    return d

ans = 0
for i in range(n):
    ans += dist(market[i])
print(ans)


