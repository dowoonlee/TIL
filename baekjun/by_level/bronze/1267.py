import sys

n = int(sys.stdin.readline())
calls = list(map(int, sys.stdin.readline().split()))

y = sum([(i//30+1)*10 for i in calls])
m = sum([(i//60+1)*15 for i in calls])

if y<m:
    print('Y %d'%y)
elif y>m:
    print('M %d'%m)
else:
    print('Y M %d'%y)
