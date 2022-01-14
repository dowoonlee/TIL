import sys
import heapq

n = int(sys.stdin.readline())

s = []
b = []
ans = []



for i in range(n):
    x = int(sys.stdin.readline())

    if len(s) == len(b):
        heapq.heappush(s, (-x, x))

    else:
        heapq.heappush(b, (x, x))

    if b and s[0][1] > b[0][0]:
        minv = heapq.heappop(b)[0]#minimum in big
        maxv = heapq.heappop(s)[1]#maximum in small
        heapq.heappush(s, (-minv, minv))
        heapq.heappush(b, (maxv, maxv))

    ans.append(s[0][1])

for i in ans:
    sys.stdout.write('%s\n'%i)

