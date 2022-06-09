import sys
from collections import deque

n = int(sys.stdin.readline())

tree = dict()
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    if tree.get(a):
        tree[a].append(b)
    else:
        tree[a] = [b]
    if tree.get(b):
        tree[b].append(a)
    else:
        tree[b] = [a]

parent = [i for i in range(n + 1)]


def dfs(root):
    dq = deque()
    dq.append(root)

    while dq:
        node = dq.pop()
        cand = tree[node]
        for c in cand:
            if parent[c] == c:
                dq.append(c)
                parent[c] = node


for i in range(1, n):
    if parent[i] == i:
        dfs(i)
    else:
        pass

for i in range(2, n + 1):
    print(parent[i])
