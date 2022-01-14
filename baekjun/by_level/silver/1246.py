import sys

n, m = map(int, sys.stdin.readline().split())
p = sorted([int(sys.stdin.readline()) for _ in range(m)])
q = [i for i in range(p[0], p[-1]+1)]
qsum = [0]*len(q)

j = 0
for i in range(len(q)):
    if q[i]>p[j]:
        j+=1
    qsum[i] = q[i] * min((len(p)-j), n)

maxq = max(qsum)

print(q[qsum.index(maxq)], maxq)