import sys

n, m = map(int, sys.stdin.readline().split())
rect = [[0]*m for _ in range(n)]
for i in range(n):
    ipt = str(sys.stdin.readline().rstrip())
    for j in range(len(ipt)):
        rect[i][j] = int(ipt[j])

#n, m = 3,5
#rect = [[4, 2, 1, 0, 1], [2, 2, 1, 0, 0], [2, 2, 1, 0, 1]]


ans = False
max_size = min(n,m)
for size in range(max_size, 1, -1):
    if ans:
        break
    for i in range(n-size+1):
        if ans:
            break
        for j in range(m-size+1):
            corners = [rect[i][j], rect[i+size-1][j], rect[i][j+size-1], rect[i+size-1][j+size-1]]
            uniq = list(set(corners))
            if len(uniq)==1:
                ans = size
                break
if ans:
    print(ans**2)
else:
    print(1)


