import sys

n,k = map(int, sys.stdin.readline().split())

flag = True
idx = 1
for i in range(1, n+1):
    if n%i==0 and idx==k:
        print(i)
        flag=False
        break
    elif n%i==0:
        idx+=1
    else:
        pass
if flag:
    print(0)
