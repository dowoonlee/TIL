import sys

n, m = map(int, sys.stdin.readline().split())
card = list(map(int,sys.stdin.readline().split()))
idxs = list(range(0, n))

sums = []

for i in idxs:
    idxs.remove(i)
    for j in idxs:
        idxs.remove(j)
        for k in idxs:
            sums.append(card[i]+card[j]+card[k])
        idxs.append(j)
    idxs = list(range(0, n))

res = sorted(list(set(sums)))
if res[-1]<=m:
    pass
else:
    nn = 0
    while res[nn]<=m:
        nn+=1
    res = res[0:nn]


abst = [100]*len(res)
for i in range(len(res)):
    abst[i] = m - res[i]
print(res[abst.index(min(abst))])