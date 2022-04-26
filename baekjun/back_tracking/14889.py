import sys
from itertools import combinations

n = int(sys.stdin.readline())

abil = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

comb = list(combinations([i for i in range(n)], n//2))
ta, tb = 0, 0


minv = n**2*100
for i in range(len(comb)//2):
    ta = comb[i]
    tb = comb[-1-i]
    tsa, tsb = 0, 0
    for j in range(len(ta)):
        for k in range(len(ta)):
            tsa += abil[ta[j]][ta[k]]
            tsb += abil[tb[j]][tb[k]]
    dif = abs(tsa-tsb)
    minv = min(dif, minv)
print(minv)

