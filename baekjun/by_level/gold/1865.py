import sys

tc = int(sys.stdin.readline())

for _ in range(tc):
    n, m, w = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(m):
        s, e, t = map(int, sys.stdin.readline().split())
        graph.append([s, e, t])
        graph.append([e, s, t])#two-way
    for _ in range(w):
        s, e, t = map(int, sys.stdin.readline().split())
        graph.append([s, e, -t])#one-way

    def bf():
        dist = [int(sys.maxsize/2)] * (n + 1)  # reset the starting node
        dist[1] = 0
        for _ in range(n-1): #to avoid the infinite cycle, set the limit as n-1
                             #n-1 is the maximum case of the hortest path(vertex-1 = the number of edges)

            for s, e, t in graph:
                if dist[s] + t < dist[e]:
                    dist[e] = dist[s] + t  #relaxation for all edges

        for s, e, t in graph:
            if dist[s] + t < dist[e]:
                return True
        return False

    if bf():
        print('YES')
    else:
        print('NO')






