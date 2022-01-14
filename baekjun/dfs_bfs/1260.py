import sys
from collections import deque


def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort(reverse=True)
                stack += temp
    return " ".join(str(i) for i in visited)

def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                queue += temp
    return " ".join(str(i) for i in visited)

n, m, v = map(int, sys.stdin.readline().split())

tgraph, graph = {}, {}
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    k = list(tgraph.keys())
    if a in k:
        tgraph[a].append(b)
    else:
        tgraph[a] = [b]
    if b in k:
        tgraph[b].append(a)
    else:
        tgraph[b] = [a]
tgraph = sorted(tgraph.items())
for i in range(len(tgraph)):
    graph[tgraph[i][0]] = sorted(tgraph[i][1])

res1, res2 = DFS(graph, v), BFS(graph, v)
print(res1)
print(res2)

