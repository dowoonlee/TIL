import sys

n = int(sys.stdin.readline())
seats = [0]*101

reject = 0
ipt = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    if seats[ipt[i]]:
        reject+=1
    else:
        seats[ipt[i]]=1
print(reject)