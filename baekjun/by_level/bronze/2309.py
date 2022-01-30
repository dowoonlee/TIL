import sys
from itertools import combinations

dwarf = [int(sys.stdin.readline()) for _ in range(9)]
sum_height = sum(dwarf)
items = [i for i in range(9)]
ans = []
comb = list(combinations(items, 2))
for out_dwarf in comb:
    sub_h = 0
    for i in out_dwarf:
        sub_h += dwarf[i]
    if sum_height-sub_h == 100:
        for i in range(9):
            if i!=out_dwarf[0] and i!=out_dwarf[1]:
                ans.append(dwarf[i])
            ans.sort()
        break
for i in ans:
    print(i)


