import sys


n, m = map(int, sys.stdin.readline().split())
bulbs = []
for _ in range(n):
    light = str(sys.stdin.readline().rstrip())
    column = []
    for l in light:
        column.append(int(l))
    bulbs.append(column)
k = int(sys.stdin.readline())


pos_row = [0]*n
for row in range(n):
    nzeros = m - sum(bulbs[row])
    if nzeros%2 == k%2 and nzeros<=k:
        pos_row[row]+=1
        compare_row = [i for i in range(n)]
        compare_row.remove(row)
        for comp in compare_row:
            if bulbs[comp] == bulbs[row]:
                pos_row[row]+=1
print(max(pos_row))





