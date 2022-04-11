import sys

n = int(sys.stdin.readline())

for i in range(n - 1):
    if i == 0:
        s0 = "*" * n
    else:
        s0 = "*" + " " * (n - 2) + "*"
    s = " " * i + s0 + " " * (2 * (n - i) - 3) + s0
    print(s)
s = " " * (n - 1) + "*" + " " * (n - 2) + "*" + " " * (n - 2) + "*"
print(s)

for i in range(n-2, -1, -1):
    if i == 0:
        s0 = "*" * n
    else:
        s0 = "*" + " " * (n - 2) + "*"
    s = " " * i + s0 + " " * (2 * (n - i) - 3) + s0
    print(s)
