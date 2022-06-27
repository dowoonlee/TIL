import sys

n = int(sys.stdin.readline())

tree = dict()
for _ in range(n - 1):
    p, c, w = map(int, sys.stdin.readline().split())
    try:
        tree[p].append((c, w))
    except KeyError:
        tree[p] = [(c, w)]
    try:
        tree[c].append((p, w))
    except KeyError:
        tree[c] = [(p, w)]

for k, v in tree.items():
    tree[k].sort(key=lambda x: x[1], reverse=True)


def dfs(root):
    max_dist = 0
    max_node = 0
    dist = [-1] * (n + 1)
    q = []
    q.append(root)
    dist[root] = 0

    while q:
        node = q.pop()
        if max_dist < dist[node]:
            max_dist = dist[node]
            max_node = node
        for next_node in tree[node]:
            if dist[next_node[0]] < 0:
                q.append(next_node[0])
                dist[next_node[0]] = dist[node] + next_node[1]
    return max_dist, max_node

if n==1:
    print(0)
else:
    _, init_node = dfs(1)
    ans, _ = dfs(init_node)
    print(ans)
