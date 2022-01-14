import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
if n==1:
    print(n**2)
else:
    data = sorted(data)
    x = data[0]*data[-1]



