import sys
import heapq

INF = sys.maxsize

ipt = sys.stdin.readline
v, e = map(int, ipt().split())
k = int(ipt())

dist = [INF] * (v + 1)

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    b, f, w = map(int, ipt().split())
    graph[b].append((f, w))

q = []
heapq.heappush(q, (0, k))
dist[k] = 0

while q:
    d, node = heapq.heappop(q)
    if dist[node] < d:
        continue
    for g in graph[node]:
        if d + g[1] < dist[g[0]]:
            dist[g[0]] = d + g[1]
            heapq.heappush(q, (d + g[1], g[0]))

for i in range(1, v + 1):
    if dist[i] >= INF:
        print("INF")
    else:
        print(dist[i])
