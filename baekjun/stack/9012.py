import sys
t = int(sys.stdin.readline())

for i in range(t):
    data = list(map(str, sys.stdin.readline().strip()))
    closed = 0
    j = 0
    while j < len(data) and closed>=0:
        if data[j]=='(':
            closed+=1
        else:
            closed-=1
        j+=1
    if closed:
       print('NO')
    else:
        print('YES')

