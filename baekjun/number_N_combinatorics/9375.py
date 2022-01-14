import sys
from itertools import combinations
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    type = []
    for j in range(n):
        c, t = map(str, sys.stdin.readline().split())
        type.append(t)

    uniq_type = sorted(list(set(type)))
    type = sorted(type)
    ntype = [0]*len(uniq_type)

    j = 0#types
    k = 0#uniq type
    while j<len(type):
        if type[j]==uniq_type[k]:
            ntype[k]+=1
            j+=1
        else:
            k+=1
    ans = 1
    for j in ntype:
        ans*=(j+1)
    print(int(ans)-1)

