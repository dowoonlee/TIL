import sys

n, m = map(int, sys.stdin.readline().split())
c_pack , c_idv = [0]*m, [0]*m

for i in range(m):
    c_pack[i], c_idv[i] = map(int, sys.stdin.readline().split())

n_pack, n_idv = n//6, n%6
min_pack, min_idv = min(c_pack), min(c_idv)

case = [min_pack*n_pack + min_idv*n_idv, min_idv*n, min_pack*(n_pack+1)]

print(min(case))