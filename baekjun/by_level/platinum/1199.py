import sys

sys.setrecursionlimit(10 ** 9)
n = int(sys.stdin.readline())
ipt = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

graph = {}

for i in range(n):
    graph[i] = []
    rsum = 0
    for j in range(n):
        rsum += 1
        graph[i].append(j)
    if rsum % 2:
        print(-1)
        sys.exit()


def search(root):
    for i in graph[root]:
        if ipt[root][i]:
            ipt[root][i] -= 1
            ipt[i][root] -= 1
            search(i)
    print(root + 1, end=" ")


search(0)
