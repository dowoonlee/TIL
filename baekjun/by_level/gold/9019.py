import sys
from collections import deque

t = int(sys.stdin.readline())

def dslr(x):
    res = [0]*4
    if 2 * x > 9999:
        res[0] = (2 * x) % 10000
    else:
        res[0] = 2 * x
    if x:
        res[1] = x - 1
    else:
        res[1] = 9999
    res[2] = x // 1000 + (x % 1000) * 10
    res[3] = (x % 10) * 1000 + x // 10
    return res


order = ["D", "S", "L", "R"]

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    cnt = [[0, 0] for _ in range(10000)]
    visited = [False]*10000
    dq = deque()
    dq.append(a)
    visited[a] = True

    while dq:
        node = dq.popleft()
        if node == b:
            break
        next_node = dslr(node)
        for i in range(4):
            if not visited[next_node[i]]:
                cnt[next_node[i]][0] = node
                cnt[next_node[i]][1] = i

                visited[next_node[i]] = True
                dq.append(next_node[i])

    ans = ""
    idx = b
    while cnt[idx][0]!=a:
        print(cnt[idx][1])
        ans += order[cnt[idx][1]]
        idx = cnt[idx][0]

    print(order[cnt[idx][1]]+ ans[::-1])
