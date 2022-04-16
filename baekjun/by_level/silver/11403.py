import sys
from collections import deque

n = int(sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = [[0]*n for _ in range(n)]

def search(root):

    visited = [0]*n
    dq = deque()
    dq.append(root)

    while dq:
        node = dq.popleft()
        #print("current:", node)
        for i in range(n):
            #print("to", i, end =" ")
            if graph[node][i] and not visited[i]:
                #print("pos")
                dq.append(i)
                visited[i] = 1
            #else:
                #print("not")
    return visited

for i in range(n):
    pos = search(i)
    for j in pos:
        print(j, end=" ")
    print()
