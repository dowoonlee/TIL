import sys

n, k = map(int ,sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split(",")))
b = a

for i in range(k):
    b = [0]*(len(a)-1)
    for j in range(len(a)-1):
        b[j] = a[j+1]-a[j]
    a = b

for i in range(len(b)):
    b[i] = str(b[i])
print(",".join(b))
