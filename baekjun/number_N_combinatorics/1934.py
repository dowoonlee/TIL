import sys

def euclid(mx, mn):
    nmin = mx%mn
    return mn, nmin

t = int(sys.stdin.readline())
for i in range(t):
    data = list(map(int,sys.stdin.readline().split()))
    x, y = max(data), min(data)
    LCM = x*y
    while y!=0:
        x, y = euclid(x, y)
    LCM /= x
    print(int(LCM))

