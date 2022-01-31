import sys

n = int(sys.stdin.readline())
wb = [[0]*100 for _ in range(100)]
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(10):
        for j in range(10):
            wb[x-1+i][y-1+j] = 1
sums = 0
for i in range(100):
    sums += sum(wb[i])
print(sums)

