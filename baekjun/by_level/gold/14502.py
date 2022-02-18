import sys
from itertools import combinations

n, m = map(int ,sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
empty_map = []
for i in range(n):
    for j in range(m):
        if lab[i][j]==0:
            empty_map.append((i, j))
def spreadout():
    return 1

x = list(combinations(empty_map, 3))
for pos in x:
    safe_place = spreadout()


