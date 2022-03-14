import sys
import heapq

t = int(sys.stdin.readline())

for _ in range(t):
    k = int(sys.stdin.readline())
    minindex, maxindex = -1, -1
    minV, maxV = sys.maxsize, -sys.maxsize
    minheap, maxheap = [], []
    visited = [False] * 1000001
    for i in range(k):
        op, n = map(str, sys.stdin.readline().split())
        n = int(n)
        if op == "I":
            heapq.heappush(minheap, (n, i))
            heapq.heappush(maxheap, (-n, i))
            visited[i] = True

        elif op=="D":
            if n==-1:
                while minheap and not visited[minheap[0][1]]:
                    heapq.heappop(minheap)
                if minheap:
                    visited[minheap[0][1]] = False
                    heapq.heappop(minheap)

            else:
                while maxheap and not visited[maxheap[0][1]]:
                    heapq.heappop(maxheap)
                if maxheap:
                    visited[maxheap[0][1]] = False
                    heapq.heappop(maxheap)

    while minheap and not visited[minheap[0][1]]:
        heapq.heappop(minheap)
    while maxheap and not visited[maxheap[0][1]]:
        heapq.heappop(maxheap)

    if minheap and maxheap:
        print(-maxheap[0][0], minheap[0][0])
    else:
        print("EMPTY")


