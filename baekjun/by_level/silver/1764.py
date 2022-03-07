import sys

n, m = map(int, sys.stdin.readline().split())

seta = set()
for _ in range(n):
    seta.add(str(sys.stdin.readline().rstrip()))
setb = set()
for _ in range(m):
    setb.add(str(sys.stdin.readline().rstrip()))

res = sorted(list(seta&setb))
print(len(res))
for i in res:
    print(i)