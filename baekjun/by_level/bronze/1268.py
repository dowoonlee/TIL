import sys
n = int(sys.stdin.readline())
d = []
for _ in range(n):
    d.append(list(map(int, sys.stdin.readline().split())))

nfr = []

for i in range(n):
    tgt = d[i]
    frs = [xx for xx in range(n)]
    frs.remove(i)
    nfrin = 0
    for k in frs:
        fr = d[k]
        for j in range(5):
            if tgt[j]==fr[j]:
                nfrin+=1
                break
    nfr.append(nfrin)

print(nfr.index(max(nfr))+1)





