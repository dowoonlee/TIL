import sys

n, m = map(int, sys.stdin.readline().split())
row, col = [0]*m, [0]*n

for i in range(n):
    guards = str(sys.stdin.readline().rstrip())
    floor = [0 if i=='.' else 1 for i in guards]
    if sum(floor)>0:
        col[i]=1
    for j in range(m):
        if floor[j]>0 and row[j]==0:
            row[j] += 1

print(max(m-sum(row), n-sum(col)))