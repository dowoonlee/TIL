import sys

curt = list(map(int, sys.stdin.readline().split(':')))
strt = list(map(int, sys.stdin.readline().split(':')))

endt = strt[:]
left = []
def h2t(time):
    return time[0]*3600+time[1]*60+time[2]

if h2t(curt)>=h2t(strt):
    endt[0]+=24
else:
    pass
for i in range(3):
    left.append(endt[i]-curt[i])

for i in range(2, -1, -1):
    if left[i]<0:
        left[i]+=60
        left[i-1]-=1
print("%02d:%02d:%02d"%(left[0], left[1], left[2]))