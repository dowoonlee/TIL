import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
cluster = int(sys.stdin.readline())

nc = 0
for i in range(n):
    if data[i]!=0:
        nc += data[i] // cluster
        if data[i] % cluster>0:
            nc+=1

print(nc*cluster)