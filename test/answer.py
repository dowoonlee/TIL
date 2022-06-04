import sys
sys.setrecursionlimit(10**5)

N, M = map(int, sys.stdin.readline().split())
node = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
p = [i for i in range(N+1)]
sorted_node = sorted(node, key=lambda x:x[2])

def find_set(x):
    if x==p[x]:
        return x
    else:
        p[x] = find_set(p[x])
        return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)
    return

length=0
idx = 0
cnt=0
while (idx<M and cnt<N):
    node1, node2, weight = node[idx][0], node[idx][1], node[idx][2]
    if find_set(node1) != find_set(node2):
        union(node1, node2)
        length += weight
        cnt+=1
    idx+=1

for i in range(1, N+1):
    find_set(i)
pset = set(p[1:])

if len(pset)!=1:
    print(-1)
else:
    print(length)
