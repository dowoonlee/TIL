import sys

x = int(sys.stdin.readline())
binx = bin(x)[2::]
s = 0
for b in binx:
    s+=int(b)
print(s)
