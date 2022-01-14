import sys

def euclid(mx, mn):
    nmin = mx%mn
    return mn, nmin


data = list(map(int,sys.stdin.readline().split()))


x, y = max(data), min(data)
LCM = x*y


while y!=0:
    x, y = euclid(x, y)
GCD = x
LCM /= GCD

print(GCD)
print(int(LCM))

