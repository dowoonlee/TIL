import sys
sys.setrecursionlimit(2000)

N, M = map(int, sys.stdin.readline().split())
node = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
p = [i for i in range(N+1)]
sorted_node = sorted(node, key=lambda x:x[2])

def find_set(x):
    if x==p[x]:
        return x
    else:
        p[x] = find_set(x)
        return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)
    return

length=0
idx = 0
cnt=0
while (idx<M or cnt<N):
    if find_set(node[idx][0]) != find_set(node[idx][1]):
        union(node[idx][0], node[idx][1])
        length += node[idx][2]
        cnt+=1
    idx+=1

pset = set(p)

if len(pset)!=1:
    print(-1)
else:
    print(length)