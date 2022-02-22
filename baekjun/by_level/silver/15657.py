import sys
from itertools import combinations_with_replacement as cwr


n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

x = list(cwr(a, m))

for i in x:
    for j in i:
        print(j, end=" ")
    print()

