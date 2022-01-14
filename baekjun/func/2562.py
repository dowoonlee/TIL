import sys

a = []
for _ in range(9):
    a.append(int(sys.stdin.readline()))
maxv= max(a)
print(maxv)
print(a.index(maxv)+1)
