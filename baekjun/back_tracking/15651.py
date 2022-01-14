import sys
from itertools import product

#n, m = map(int, sys.stdin.readline().split())

n, m = 3, 3


arr = [i+1 for i in range(n)]
ans = list(product(arr, repeat=m))

for i in ans:
    x = ''
    for j in range(len(i)):
        if j==len(i)-1:
            x += '%d'%i[j]
        else:
            x += '%d ' % i[j]
    print(x)


