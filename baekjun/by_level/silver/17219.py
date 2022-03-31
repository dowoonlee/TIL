import sys

n, m = map(int, sys.stdin.readline().split())


data = dict()

for _ in range(n):
    s, p = map(str, sys.stdin.readline().split())
    data[s] = p


for _ in range(m):
    print(data[sys.stdin.readline().rstrip()])

