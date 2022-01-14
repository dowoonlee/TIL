import sys

def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)

n, k = map(int, sys.stdin.readline().split())


def fts(x):
    flim = 0
    while x > (5 ** flim):
        flim+=1
    tlim = 0
    while x > (2 ** tlim):
        tlim+=1
    fives, twos = 0, 0
    for i in range(flim):
        fives += x//(5**(i+1))
    for i in range(tlim):
        twos += x//(2**(i+1))
    return fives, twos

fnum, tnum = fts(n)
fdeno0, tdeno0 = fts(k)
fdeno1, tdeno1 = fts(n-k)
fts = [fnum-fdeno0-fdeno1, tnum-tdeno0-tdeno1]
print(int(min(fts)))
