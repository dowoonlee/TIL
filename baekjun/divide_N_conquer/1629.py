import sys

a, b, c = map(int, sys.stdin.readline().split())

binb = bin(b)[2::]
modb = [0]*len(binb)
modb[0] = a%c


for i in range(len(binb)-1):
    modb[i+1] = (modb[i] * modb[i])%c



x = 1

for i in range(len(modb)):
    if int(binb[::-1][i]):
        x *= modb[i]

print(x%c)


