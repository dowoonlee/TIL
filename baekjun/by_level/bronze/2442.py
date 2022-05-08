import sys

n = int(sys.stdin.readline())

for i in range(n):
    ns = 2*i+1
    nb = n-i-1
    print(" "*nb+"*"*ns)