import sys

n, k = map(int, sys.stdin.readline().split())

child = [[0]*2 for _ in range(6)]

for _ in range(n):
    s, y = map(int, sys.stdin.readline().split())
    child[y-1][s]+=1

ans = 0
for y in range(6):
    for s in range(2):
        numb = child[y][s]
        if not numb:
            pass
        else:
            ans += numb//k + bool(numb%k)
print(ans)


