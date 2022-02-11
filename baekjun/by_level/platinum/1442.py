import sys

#l, r = map(int, sys.stdin.readline().split())
#ldigit, rdigit = len(bin(l))-2, len(bin(r))-2

def way(n):
    i = 0
    sums = 0
    while n >= 1+2*i:
        fac = 1
        for j in range(i):
            fac *= (n-1-2*i-j)
            fac /= j+1
        sums += fac
        i+=1
    return int(2 * sums)
print(way(3))