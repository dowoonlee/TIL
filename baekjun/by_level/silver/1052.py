import sys

n, k = map(int, sys.stdin.readline().split())

cup = 0
while (bin(n).count("1"))>k:
    add = 2**(bin(n)[::-1].index("1"))
    cup += add
    n += add
print(cup)